from contextlib import asynccontextmanager

import grpc
from proto.remote.kv_pb2 import Cursor, Op
from proto.remote.kv_pb2_grpc import KVStub


class ErigonKV:
    async def connect(self, private_api="127.0.0.1:9090"):
        self.channel = grpc.aio.insecure_channel(private_api)
        self.stub = KVStub(self.channel)
        self.conn = self.stub.Tx()
        await self.conn.read()

    @asynccontextmanager
    async def open(self, bucket, dup_sort=False):
        """
        async with kv.open('bucket') as cursor:
            await cursor.seek(b'prefix')

            async for row in cursor:
                print(row)
        """
        op = Op.OPEN_DUP_SORT if dup_sort else Op.OPEN
        await self.conn.write(Cursor(op=op, bucketName=bucket))
        cursor = await self.conn.read()
        try:
            yield ErigonCursor(self.conn, cursor.cursorID)
        finally:
            await self.conn.write(Cursor(op=Op.CLOSE, cursor=cursor.cursorID))
            await self.conn.read()


class ErigonCursor:
    def __init__(self, conn, cursor, dup_sort=False):
        self.conn = conn
        self.cursor = cursor
        self.dup_sort = dup_sort

    def __aiter__(self):
        return self

    async def __anext__(self):
        op = Op.NEXT_DUP if self.dup_sort else Op.NEXT
        return await self.read(op)

    async def read(self, op, key=None, value=None):
        await self.conn.write(Cursor(op=op, k=key, v=value, cursor=self.cursor))
        row = await self.conn.read()
        if row.k == b"":
            raise StopAsyncIteration
        return row

    async def seek(self, key):
        return await self.read(Op.SEEK, key=key)

    async def seek_exact(self, key):
        return await self.read(Op.SEEK_EXACT, key=key)

    async def first(self):
        return await self.read(Op.FIRST)

    async def last(self):
        return await self.read(Op.LAST)

    async def prev(self):
        return await self.read(Op.PREV)

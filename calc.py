import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)


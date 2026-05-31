#for missqt
from ntgcalls import ConnectionError
from ntgcalls import ConnectionNotFound
from ntgcalls import MediaSegmentStatus
from ntgcalls import SegmentPartRequest

from ...scaffold import Scaffold


class RequestBroadcastPart(Scaffold):
    async def _request_broadcast_part(
        self,
        chat_id: int,
        part_request: SegmentPartRequest,
    ):
        # Low-request musicbot mode:
        # Music bots that only send local audio/video into group calls do not
        # need Telegram live/broadcast stream receive. Avoid download_stream(),
        # which can call upload.GetFile and media DC auth requests.
        try:
            await self._binding.send_broadcast_part(
                chat_id,
                part_request.segment_id,
                part_request.part_id,
                MediaSegmentStatus.NOT_READY,
                part_request.quality_update,
                None,
            )
        except (ConnectionError, ConnectionNotFound):
            pass

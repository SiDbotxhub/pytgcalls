#for missqt
from ntgcalls import ConnectionError
from ntgcalls import ConnectionNotFound

from ...scaffold import Scaffold


class RequestBroadcastTimestamp(Scaffold):
    async def _request_broadcast_timestamp(
        self,
        chat_id: int,
    ):
        # Low-request musicbot mode:
        # Do not query Telegram for live/broadcast stream timestamps. Normal
        # outbound musicbot audio/video playback does not need this feature.
        try:
            await self._binding.send_broadcast_timestamp(
                chat_id,
                0,
            )
        except (ConnectionError, ConnectionNotFound):
            pass

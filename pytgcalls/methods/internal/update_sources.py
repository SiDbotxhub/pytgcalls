#for missqt
from typing import Union

from ...scaffold import Scaffold


class UpdateSources(Scaffold):
    async def _update_sources(
        self,
        chat_id: Union[int, str],
    ):
        # Low-request musicbot mode:
        # This bot only sends outbound audio/video to group calls.
        # Incoming camera/screen-share source discovery is intentionally
        # skipped to avoid extra GetGroupParticipants requests on play/switch.
        return

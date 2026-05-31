from typing import Union

from ...scaffold import Scaffold


class UpdateSources(Scaffold):
    async def _update_sources(
        self,
        chat_id: Union[int, str],
    ):
        # Low-request musicbot mode:
        # Normal outbound audio/video playback does not need to scan other
        # participants for incoming camera/presentation sources.
        # Skipping this avoids extra GetGroupParticipants requests.
        return

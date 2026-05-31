import logging

from ntgcalls import MediaState

from ...scaffold import Scaffold

py_logger = logging.getLogger('pytgcalls')


class UpdateStatus(Scaffold):
    async def _update_status(self, chat_id: int, state: MediaState):
        try:
            peer = self._cache_user_peer.get(chat_id)
            if peer is None:
                return

            status_key = (
                bool(state.muted),
                bool(state.video_paused),
                bool(state.video_stopped),
                bool(state.presentation_paused),
            )
            if not hasattr(self, '_last_group_call_status'):
                self._last_group_call_status = {}
            if self._last_group_call_status.get(chat_id) == status_key:
                return
            self._last_group_call_status[chat_id] = status_key

            await self._app.set_call_status(
                chat_id,
                state.muted,
                state.video_paused,
                state.video_stopped,
                state.presentation_paused,
                peer,
            )
        except Exception as e:
            py_logger.debug(f'SetVideoCallStatus: {e}')

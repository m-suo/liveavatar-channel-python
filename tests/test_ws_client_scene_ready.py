from __future__ import annotations

import asyncio

import pytest

from liveavatar_channel_sdk._ws_client import _AvatarWsClient
from liveavatar_channel_sdk.message_builder import MessageBuilder


class FakeCallbacks:
    def __init__(self) -> None:
        self.scene_ready_count = 0

    async def on_scene_ready(self) -> None:
        self.scene_ready_count += 1


@pytest.mark.asyncio
async def test_ws_client_routes_scene_ready_to_callbacks():
    callbacks = FakeCallbacks()
    client = _AvatarWsClient(
        "ws://example.invalid",
        callbacks,
        asyncio.Event(),
    )

    await client._handle_text('{"event":"scene.ready"}')

    assert callbacks.scene_ready_count == 1


def test_scene_ready_builder_has_no_payload():
    assert MessageBuilder.scene_ready() == {"event": "scene.ready"}

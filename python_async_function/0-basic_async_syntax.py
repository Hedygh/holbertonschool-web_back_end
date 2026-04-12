#!/usr/bin/env python3
""" basyc async syntax """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Randomized float return"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

import pytest
import pygame
import random
from ghost import Ghost


@pytest.fixture
def ghost(monkeypatch):
    # Fix direction randomness for predictable tests
    monkeypatch.setattr(random, "choice", lambda x: "right")
    return Ghost(100, 100, (255, 0, 0))  # red ghost


@pytest.fixture
def player():
    class DummyPlayer:
        def __init__(self):
            self.x = 150
            self.y = 100
    return DummyPlayer()


@pytest.fixture
def walls():
    return [
        pygame.Rect(0, 0, 20, 600),      # Left wall
        pygame.Rect(200, 200, 20, 20),   # Small obstacle
        pygame.Rect(780, 0, 20, 600),    # Right wall
    ]


def test_ghost_initialization(ghost):
    assert ghost.x == 100
    assert ghost.y == 100
    assert ghost.color == (255, 0, 0)
    assert ghost.speed == 1
    assert ghost.radius == 10
    assert ghost.direction in ["right", "left", "up", "down"]
    assert not ghost.scared


def test_ghost_movement_no_walls(ghost, player):
    initial_x = ghost.x
    initial_y = ghost.y

    ghost.direction = "right"
    ghost.move([], player)
    assert ghost.x == initial_x + ghost.speed
    assert ghost.y == initial_y

    ghost.direction = "left"
    ghost.move([], player)
    assert ghost.x == initial_x  # moved left, back to start
    assert ghost.y == initial_y


def test_ghost_collision_with_walls(ghost, walls, player):
    # Move into left wall
    ghost.x = 25
    ghost.y = 100
    ghost.direction = "left"
    ghost.move(walls, player)
    assert ghost.x == 25  # should not move through wall

    # Move into small obstacle
    ghost.x = 190
    ghost.y = 210
    ghost.direction = "right"
    ghost.move(walls, player)
    assert ghost.x == 190  # should stay due to collision


def test_ghost_scared_timer(ghost, player):
    ghost.scared = True
    ghost.scared_timer = 2
    ghost.direction = "right"

    ghost.move([], player)
    assert ghost.scared_timer == 1
    assert ghost.scared  # still scared

    ghost.move([], player)
    assert ghost.scared_timer == 0
    assert not ghost.scared  # should reset after timer ends


def test_ghost_moves_toward_player(ghost, player, monkeypatch):
    # Force random.random() to always be > 0.1 so ghost follows player
    monkeypatch.setattr(random, "random", lambda: 0.5)
    ghost.x = 100
    ghost.y = 100

    # Player to the right
    player.x = 200
    player.y = 100
    ghost.move([], player)
    assert ghost.direction == "right"

    # Player above
    player.x = 100
    player.y = 50
    ghost.move([], player)
    assert ghost.direction == "up"

import pytest
import pygame
from game_board import GameBoard
from item import Pellet, PowerPellet # importing this to test the location of the pellets and walls don't collide

@pytest.fixture
def game_board():
    return GameBoard()

@pytest.fixture
def walls():
    board = GameBoard() # since all gameboards have the same walls
                        # I'm just going to create a new one to get its walls
    return board.walls
    

def test_game_board_initialization(game_board):
    assert game_board.width == 800
    assert game_board.height == 600
    assert len(game_board.walls) == 8
    assert len(game_board.power_pellets) == 4

def test_outer_walls_dimensions(game_board):
    outer_walls = game_board.walls[:4]  # The first four are outer walls
    top, left, bottom, right = outer_walls

    assert top.size == (game_board.width, 20)
    assert left.size == (20, game_board.height)
    assert bottom.size == (game_board.width, 20)
    assert right.size == (20, game_board.height)

    assert top.topleft == (0, 0)
    assert left.topleft == (0, 0)
    assert bottom.bottomleft == (0, game_board.height)
    assert right.topright == (game_board.width, 0)

def test_inner_walls_positions(game_board):
    inner_walls = game_board.walls[4:]
    wall1, wall2, wall3, wall4 = inner_walls

    assert (wall1.x, wall1.y, wall1.width, wall1.height) == (100, 100, 20, 200)
    assert (wall2.x, wall2.y, wall2.width, wall2.height) == (300, 100, 200, 20)
    assert (wall3.x, wall3.y, wall3.width, wall3.height) == (600, 100, 20, 400)
    assert (wall4.x, wall4.y, wall4.width, wall4.height) == (300, 350, 200, 20)

def test_pellets_do_not_overlap_with_walls(game_board):
    for pellet in game_board.pellets:
        pellet_pos = (pellet.x, pellet.y)
        for wall in game_board.walls:
            assert not wall.collidepoint(pellet_pos)


def test_power_pellet_positions(game_board):
    pellet1, pellet2, pellet3, pellet4 = game_board.power_pellets
    
    assert (pellet1.x, pellet1.y) == (50, 50)
    assert (pellet2.x, pellet2.y) == (game_board.width - 50, 50)
    assert (pellet3.x, pellet3.y) == (50, game_board.height - 50)
    assert (pellet4.x, pellet4.y) == (game_board.width - 50, game_board.height - 50)

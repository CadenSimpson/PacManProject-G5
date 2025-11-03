import pytest
import pygame
from item import Pellet, PowerPellet

@pytest.fixture
def pellet():
    return Pellet(50, 50)

@pytest.fixture
def power_pellet():
    return PowerPellet(100, 100)


def test_pellet_initialization(pellet):
    # pellet initializes with correct values
    assert pellet.x == 50
    assert pellet.y == 50
    assert pellet.radius == 2
    assert pellet.collected is False


def test_power_pellet_initialization(power_pellet):
    # power pellet initializes with correct values
    assert power_pellet.x == 100
    assert power_pellet.y == 100
    assert power_pellet.radius == 8
    assert power_pellet.collected is False


def test_pellet_collected_state(pellet):
    # pellet collected state can be changed
    assert pellet.collected is False
    
    pellet.collected = True
    assert pellet.collected is True


def test_pellet_radius_difference():
    # pellets and power pellets have different sizes
    pellet = Pellet(0, 0)
    power_pellet = PowerPellet(0, 0)
    
    assert pellet.radius < power_pellet.radius
    assert pellet.radius == 2
    assert power_pellet.radius == 8


def test_pellet_with_float_coordinates():
    # bug: Pellet accepts float coordinates, pygame.draw.circle requires integers.
    # test shows that Pellet doesn't validate or convert coordinate types
        
    # Create pellet with float coordinates
    pellet = Pellet(50.5, 75.3)
    
    # Pellet stores float values without validation
    assert pellet.x == 50.5
    assert pellet.y == 75.3
    
    # Initialize pygame to test drawing
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    # fails because pygame.draw.circle expects integer coordinates
    with pytest.raises(TypeError):
        pellet.draw(screen)
    
    pygame.quit()
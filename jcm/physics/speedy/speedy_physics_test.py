import unittest

class TestSpeedyPhysicsUnit(unittest.TestCase):
    def setUp(self):
        global PhysicsState, SpeedyPhysics, ForcingData, Parameters, TerrainData, DateData
        from jcm.physics_interface import PhysicsState
        from jcm.physics.speedy.speedy_physics import SpeedyPhysics
        from jcm.forcing import ForcingData
        from jcm.physics.speedy.params import Parameters
        from jcm.terrain_data import TerrainData
        from jcm.utils import get_coords
        from jcm.date import DateData

    def test_speedy_forcing(self):
        grid_shape = (8,1,1)
        tendencies, data = SpeedyPhysics().compute_tendencies(
            state=PhysicsState.zeros(grid_shape),
            forcing=ForcingData.ones(grid_shape[1:]),
            geometry=TerrainData.single_column(num_levels=grid_shape[0]),
            date=DateData.zeros()
        )
        self.assertIsNotNone(tendencies)
        self.assertIsNotNone(data)
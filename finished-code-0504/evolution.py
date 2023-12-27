class Evolution:
    def __init__(self, population_count, keep_count):
        self.population_count = population_count
        self.keep_count = keep_count

    def execute(self, weighted_chromosomes):
        # selection
        sorted_chromosomes = [weighted_chromosome.chromosome for weighted_chromosome in sorted(weighted_chromosomes)]
        keep_chromosomes = sorted_chromosomes[:self.keep_count]

        # cross over
        offspring = []

        # mutation

        assert len(offspring) == self.population_count, "Offspring count is not population_count"
        return offspring
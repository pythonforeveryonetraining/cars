class Evolution:
    def __init__(self, population_count, keep_count):
        self.population_count = population_count
        self.keep_count = keep_count
        
    def execute(self, rankable_chromosomes):
        # selection
        sorted_chromosomes = [w.chromosome for w in sorted(rankable_chromosomes)]
        keep_chromosomes = sorted_chromosomes[:self.keep_count]
        
        # cross over
        offspring = []
        
        # mutation
        
        assert len(offspring) == self.population_count, "Offspring count is not population_count"
        return offspring
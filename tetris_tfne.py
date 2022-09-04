import tfne

#install tfne with: pip install tfne
#pip install graphviz to visualise nodes with: pip install graphviz

config = tfne.parse_configuration('./config-file.cfg')

# Supply path to a backup serving as the initial state
ne_algorithm = tfne.algorithms.CoDeepNEAT(config,
                                          initial_state_file_path='./tfne_state_backup_gen_15.json')

environment = tfne.environments.CIFAR10nvironment(weight_training=True,
                                                  config=config,
                                                  verbosity=0)

# Alternative, though identical, creation of the environment specifying parameters explicitly
# instead of through the config
environment_alt = tfne.environments.CIFAR10nvironment(weight_training=True,
                                                      verbosity=0, #
                                                      epochs=8 #the no. of times the alg will use the entire training set
                                                      batch_size=None)

#serialization and deserialization
# Train and save best genome
best_genome = engine.train()
best_genome_file_path = best_genome.save_genotype(save_dir_path='./')

# Load the serialized best genome and get the encoded TF model
loaded_genome = tfne.deserialization.load_genome(best_genome_file_path)
tf_model = loaded_genome.get_model()

# Alternatively, it is also possible to save the TF model directly
best_genome.save_model(file_path='./best_genome_model/')

environment = tfne.environments.CIFAR10nvironment(weight_training=True,
                                                  config=config,
                                                  verbosity=0)

# Alternative, though identical, creation of the environment specifying parameters explicitly
# instead of through the config
environment_alt = tfne.environments.CIFAR10nvironment(weight_training=True,
                                                      verbosity=0,
                                                      epochs=8
                                                      batch_size=None)

engine = tfne.EvolutionEngine(ne_algorithm=ne_algorithm,
                              environment=environment,
                              backup_dir_path='./',
                              max_generations=64,
                              max_fitness=100.0)

best_genome = engine.train()
print("Best genome returned by evolution:\n")
print(best_genome)
# BacwardChainingZooKeeper
Backward Chaining implementation for Zookeeper problem

Example Output:

Initial working memory: ['has feathers', 'lays eggs', 'swims', 'does not fly', 'is black and white', 'has tawny color', 'exit'] 

There would be waits for user input in the remaining part to check the current situation
Please press the enter to continue execution. 

Initial hypothesis:  is a penguin

Rule Z14 is fired
Rule Z14=> anticedents: ['is a bird', 'does not fly', 'swims', 'is black and white'], consequent: is a penguin

Rule Z3 is fired
Rule Z3=> anticedents: ['has feathers'], consequent: is a bird

It is a bird
Current working memory: ['has feathers', 'lays eggs', 'swims', 'does not fly', 'is black and white', 'has tawny color', 'exit', 'is a bird'] 


It is a penguin
Current working memory: ['has feathers', 'lays eggs', 'swims', 'does not fly', 'is black and white', 'has tawny color', 'exit', 'is a bird', 'is a penguin'] 


Hypothesis it is a penguin TRUE

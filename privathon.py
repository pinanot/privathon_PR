import builtins as __builtin__

'''
# privathon.py

private scoped python

## RESOURCES

1. 0 CONSTANTS
2. 1 LAMBDAS
3. FUNCTIONS
4. CLASSES

### 0 CONSTANTS

1. 0 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 1. 0 builtin scope

 - end

#### 2. 0 public scope

 - end

#### 3. 0 local scope

 - end

#### 4. 0 private scope

 - end

### LAMBDAS

1. builtin scope
2. public scope
3. local scope
4. private scope

'''

__builtin__.__on_builtin_scope__ = lambda name : lambda value : setattr(__builtin__, name, value)

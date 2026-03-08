from martialaw import martialaw as __clsr__
import builtins as __builtin__

"""
# privathon.py

private scoped python

## DEPENDENCY

1. 1 modules
2. 1 module::functions
3. 0 module::all_functions

### 1 modules

 - builtins as __builtin__
 - end

### 1 module::functions

 - martialaw::martialaw as __clsr__
 - end

### 0 module::all_functions

 - end

## RESOURCES

1. 1 CONSTANTS
2. 4 LAMBDAS
3. 1 FUNCTIONS
4. 1 CLASSES

### 1 CONSTANTS

1. 1 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 1 builtin scope

 - constant_err = ConstantError("const is immutable")

 ```markdown
 # constant_err

 writing...
 ```

 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 4 LAMBDAS

1. 4 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 4 builtin scope

 - __set_builtin_scope__ = __clsr__(lambda name, value : setattr(__builtin__, name, value))

````markdown
# @__set_builtin_scope__(name : str) decorator

set name as (name : str) to set var in builtin scope

## for example

1. variable

```python
@__set_builtin_scope__("example")
_ = 45510

print(example == 45510) # True
```

2. lambda

```python
@__set_builtin_scope__("example")
_ = lambda : 45510

print(example() == 45510) # True
```

3. function

```python
@__set_builtin_scope__("example")
def example():
    return 45510

print(example() == 45510) # True
```

4. class

```python
@__set_builtin_scope__("AmamiyaGoro")
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"

class HoshinoAkuamarin(AmamiyaGoro):
    def __str__(self):
        return "Social ills"
```

 - fin -
````

 - __on_builtin_scope__ = lambda named_obj : __set_builtin_scope__(named_obj.__name__, named_obj)

````markdown
# @__on_builtin_scope__ decorator

1. function

```python
@__on_builtin_scope__
def example():
    return 45510
```

is

```python
@__set_builtin_scope__("example")
def example():
    return 45510
```

2. class

```python
@__on_builtin_scope__
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"
```

is

```python
@__set_builtin_scope__("AmamiyaGoro")
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"
```

- fin -
````

 - getter_and_setter = __clsr__(lambda getter, setter : property(fget = getter, fset = setter))

````markdown
# @getter_and_setter decorator

## for example to make property "example"

```python
@getter_and_setter
def example(self):
    return 45510

@example
def example(self, value):
    raise AttributeError("constant is immutable")
```

````

 - const = lambda constant_function : getter_and_setter(constant_function)(raise_constant_err)

````markdown
# @const decorator

 - fin -
````
 
 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 1 FUCNTIONS

1. 1 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 0 builtin scope

 - raise_constant_err
 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 1 CLASSES

1. 1 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 0 builtin scope

 - ConstantError
 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

"""

@__clsr__
__builtin__.__set_builtin_scope__ = lambda name, value : setattr(__builtin__, name, value)

@__set_builtin_scope__("__builtin_scope__")
__on_builtin_scope__ = lambda named_obj : __set_builtin_scope__(named_obj.__name__, named_obj)

@__on_builtin_scope__("getter_and_setter")
@__clsr__
getter_and_setter = lambda getter, setter : property(fget = getter, fset = setter)

@__builtin_scope__
class ConstantError(Exception):
    """
    # error ConstantError

    writing...

     - fin -
    """
     
    pass

@__on_builtin_scope__("constant_err")
constant_err = ConstantError("const is immutable")

@__builtin_scope__
def raise_constant_err():
    """
    # function raise_constant_err()

    writing...

     - fin -
    """
    raise constant_err

@__on_builtin_scope__("const")
const = lambda constant_function : getter_and_setter(constant_function)(raise_constant_err)

def static(var):
    @getter_and_setter(lambda self : var)
    def ret(self, value):
        nonlocal var
        var = value
    return ret
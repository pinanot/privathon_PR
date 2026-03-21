from time import time as _unix_time
from random import random as _random_of_unit_interval
from types import SimpleNamespace as namespace
from martialaw.martialaw import martialaw as __clsr__
from martialaw.martialaw import partial as _partial
from functools import wraps as _smart_deco_wraps
import builtins as __builtin__

"""
# privathon.py

private scoped python

## DEPENDENCY

1. 1 modules
2. 6 module::functions / module::classes
3. 0 module::all_resource

### 1 modules

 - builtins as __builtin__
 - end

### 1 module::functions / module::classes

 - martialaw.martialaw::martialaw as __clsr__
 - martialaw.martialaw::partial as _partial
 - functools::wraps as _smart_deco_wraps
 - types::SimpleNamespace as namespace
 - time::time as _unix_time
 - random::random as _random_of_unit_interval
 - end

### 0 module::all_resource

 - end

## RESOURCES

1. 1 CONSTANTS
2. 7 LAMBDAS
3. 1 FUNCTIONS
4. 4 CLASSES

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

### 7 LAMBDAS

1. 7 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 5 builtin scope

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

 - call_constant_functor = lambda f : f()

````markdown
# function call_constant_functor

 - fin -
````

 - salt = lambda : hash(str(_unix_time() + _random_of_unit_interval()))

````markdown
# function salt

 - fin -
````

 - salted_pw = lambda pw: f"{salt()}{pw}"

````markdown
# function salted_pw

 - fin -
````

 - functional_view = __clsr__(lambda real_f, view_f : __smart_deco_wraps__(view_f)(real_f)

````markdown
# decorator @functional_view(real_f)

 - fin - 
````

 - fview = functional view

tip : fview is just another name of functional view

 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 1 FUCNTIONS

1. 0 builtin scope
2. 1 public scope
3. 0 local scope
4. 0 private scope

#### 0 builtin scope

 - end

#### 1 public scope

 - raise_constant_err
 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 5 CLASSES

1. 2 builtin scope
2. 3 public scope
3. 0 local scope
4. 0 private scope

#### 1 builtin scope

 - ConstantError
 - end

#### 3 public scope

 - private
 - PrivateObject
 - LibOb
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

@__set_builtin_scope__("call_constant_functor")
call_constant_functor = lambda f : f()

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

def raise_constant_err():
    """
    # function raise_constant_err()

    writing...

     - fin -
    """
    raise constant_err

@__set_builtin_scope__("salt")
salt = lambda : hash(str(_unix_time() + _random_of_unit_interval()))

@__set_builtin_scope__("salted_pw")
salted_pw = lambda pw : f"{salt()}{pw}"

@__set_builtin_scope__("functional_view")
functional_view = __clsr__(lambda real_f, view_f : _smart_deco_wraps(view_f)(real_f))

__set_builtin_scope__("fview")(functional_view)

class private(type):
    """
    # metaclass private
    
    ## as metaclass

    writing...
    
    ## static methods
    
    1. 9 LAMBDAS
    2. 2 FUNCTIONS

    ### 5 LAMBDAS
    
     - sealed_value = lambda value : const(lambda self : value)
    
    ````markdown
    # function sealed_value
    
     - fin -
    ````

     - static = __clsr__(lambda __static__,     func : _smart_deco_wraps(_partial(func, __static__ = __static__)))
    
    ````markdown
    # @static(__static__) decorator
    
     - fin -
    ````
    
     - static_decocls = lambda cls : static(call_constant_functor(cls))
    
    ````markdown
    # decorator static_decocls
    
     - fin -
    ````
    
     - end
    
    ## 1 FUNCTIONS
    
    - sealed_value
    - end
    
    ## as for lib

    writing...
    
     - fin -
    """
    
    @staticmethod
    @__clsr__
    seal = lambda getter, setter : property(fget = getter, fset = setter)

    @staticmethod
    const = lambda constant_function : private.seal(constant_function)(raise_constant_err)

    @staticmethod
    def sealed_value(var):
        """
        # function sealed_value
        
         - fin -
        """
        @private.seal(lambda self : var)
        def ret(self, value):
            nonlocal var
            var = value
        return ret

    @staticmethod
    const_value = lambda value : private.const(lambda self : value)

    @staticmethod
    @__clsr__
static = lambda __static__, func : _smart_deco_wraps(_partial(func, __static__ = __static__))

    @staticmethod
    static_decocls = lambda cls : static(call_constant_functor(cls))
    
    def __new__(metacls, name, *argv):
        """
        # privathon private class real constructor
        
         - fin -
        """
        return metacls.__new_core__(name, *argv)
    
    def __new_core__(metacls, name, *argv, pop_self_flag = True):
        """
        # privathon private class fake constructor
        
        ## as constructor
        ## as function
        
         - fin -
        """
        L = len(argv)
        assert L * L == L + L, f"private get 1 or 3 arguments but {L} given" # L(L - 2) = 0 ↔ L = 0 ∨ L = 2
        
        if L: # L == 2. check "as constructor
            __dict__ = argv[1]
            @const
            def private(self, private_wraps = {}):
                selfid = id(self)
                if selfid in private_wraps: return private_wraps[selfid]
                else:
                    this = self
                    __private__ = __dict__["private"]()
                    @const
                    def private(self):
                        if pop_self_flag: del self
                        return this
                    def __del__(self):
                        __dict__["__del__"](self)
                        del private_wraps[selfid]
                    return type(
                       "PrivateWrapper",
                       (),
                       {
                           i : (
                               private if i == "private" else ( # as ob : PrivateWrapper, ob.private is original ob of private
                               __del__ if i == "__del__" else (
                               _smart_deco_wraps(j)(_partial(j, this = self, __private__ = __private__)) if callable(j) else j
                               )
                               )
                           ) for i, j in __dict__.items() if i != "__init__"
                       }
                   )
           return type(
               metacls,
               name,
               argv[0],
               {
                   i : (
                       private if i == "private" else (
                       _smart_deco_wraps(j)(_partial(j, this = metacls, __private__ = metacls)) if callable(j) else j
                   )
                   ) for i, j in __dict__.items()
               }
           )
        else: return name.private # if L == 1 then just return private. check "as function"

class PrivateObject(private):
    """
    # PrivateObject
    
     - fin -
    """
    def __new__(metacls, name, *argv):
        """
        # class PrivateObject constructor

        ...writing...
        """
        return metacls.__new_core__(name, *argv, pop_self_flag = False)

@__on_builtin_scope__
class LibOb(metaclass = PrivateObject):
    """
    # LibOb
    
     - fin -
    """
    class private:
        data = private.sealed_value({})
        deco = private.sealed_value(private.static)
    
    def assertize_object(self, this, __private__):
        """
        # method assertize_object
        
         - fin -
        """
        assert this != self, f"LibOb should be private object (PrivateWrapper), not public object {this} (LibOb), but {self} (self) is public"
    
    def __call__(self, libname, pw, this, __private__):
        """
        # LibOb object(libname, pw)
        
         - fin -
        """
        self.assertize_object()
        if libname in __private__.data: assert __private__.data[libname][0] == hash(pw), "permission denied"
        else: __private__.data[libname] = (hash(pw), {})
        
        class LibObExporter:
            """
            # class LibObExporter
            
             - fin -
            """
            @private.static(__private__.data[libname][1])
            def __setattr__(self, varname, value, __static__):
                """
                # LibObExporter object.[varname] = value
                
                 - fin -
                """
                __static__[varname] = value
            
            def __getattr__(self, varname):
                """
                # LibObExporter decorator @object.[varname]
                
                 - fin -
                """
                def deco(value):
                    return self.__setattr__(varname, value)
                return deco
            
            def __neg__(self):
                """
                # LibObExporter decorator @(-object)
                
                 - fin -
                """
                def deco(decorable):
                    return self.__setattr__(decorable.__name__, value)
                return deco
        return LibObExporter()
    
    def __getattr__(self, libname, this, __private__):
        """
        # LibOb object.[libname]
        
         - fin -
        """
        self.assertize_object()
        assert libname in __private__.data, f"lib not found error : no libname {libname} is this LibOb {this}'s {self}"
        
        if __private__.deco == private.static: __private__.deco = __private__.deco = __private__(__private__.data[libname][1])
        
        class LibObImporter:
            """
            # class LibObImporter
            
             - fin -
            """
            @private.static(__private__.data[libname][1])
            def __getattr__(self, varname, __static__):
                return __static__[varname]
        
        return LibObImporter()
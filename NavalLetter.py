# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_NavalLetter', [dirname(__file__)])
        except ImportError:
            import _NavalLetter
            return _NavalLetter
        if fp is not None:
            try:
                _mod = imp.load_module('_NavalLetter', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _NavalLetter = swig_import_helper()
    del swig_import_helper
else:
    import _NavalLetter
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _NavalLetter.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _NavalLetter.SwigPyIterator_value(self)
    def incr(self, n=1): return _NavalLetter.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _NavalLetter.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _NavalLetter.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _NavalLetter.SwigPyIterator_equal(self, *args)
    def copy(self): return _NavalLetter.SwigPyIterator_copy(self)
    def next(self): return _NavalLetter.SwigPyIterator_next(self)
    def __next__(self): return _NavalLetter.SwigPyIterator___next__(self)
    def previous(self): return _NavalLetter.SwigPyIterator_previous(self)
    def advance(self, *args): return _NavalLetter.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _NavalLetter.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _NavalLetter.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _NavalLetter.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _NavalLetter.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _NavalLetter.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _NavalLetter.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _NavalLetter.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class WordProcessingCompiler(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WordProcessingCompiler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WordProcessingCompiler, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["getInstance"] = lambda x: _NavalLetter.WordProcessingCompiler_getInstance
    if _newclass:getInstance = staticmethod(_NavalLetter.WordProcessingCompiler_getInstance)
    __swig_destroy__ = _NavalLetter.delete_WordProcessingCompiler
    __del__ = lambda self : None;
    def compile(self, *args): return _NavalLetter.WordProcessingCompiler_compile(self, *args)
    def setTempDir(self, *args): return _NavalLetter.WordProcessingCompiler_setTempDir(self, *args)
    def getWorkDir(self): return _NavalLetter.WordProcessingCompiler_getWorkDir(self)
    def getTempDir(self): return _NavalLetter.WordProcessingCompiler_getTempDir(self)
WordProcessingCompiler_swigregister = _NavalLetter.WordProcessingCompiler_swigregister
WordProcessingCompiler_swigregister(WordProcessingCompiler)

def WordProcessingCompiler_getInstance():
  return _NavalLetter.WordProcessingCompiler_getInstance()
WordProcessingCompiler_getInstance = _NavalLetter.WordProcessingCompiler_getInstance

class WordProcessingMerger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WordProcessingMerger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WordProcessingMerger, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["getInstance"] = lambda x: _NavalLetter.WordProcessingMerger_getInstance
    if _newclass:getInstance = staticmethod(_NavalLetter.WordProcessingMerger_getInstance)
    __swig_destroy__ = _NavalLetter.delete_WordProcessingMerger
    __del__ = lambda self : None;
    def load(self, *args): return _NavalLetter.WordProcessingMerger_load(self, *args)
    def save(self, p_fileName=""): return _NavalLetter.WordProcessingMerger_save(self, p_fileName)
    def _print(self, *args): return _NavalLetter.WordProcessingMerger__print(self, *args)
    def setClipboardValue(self, *args): return _NavalLetter.WordProcessingMerger_setClipboardValue(self, *args)
    def paste(self, p_itemName=""): return _NavalLetter.WordProcessingMerger_paste(self, p_itemName)
    def getFields(self): return _NavalLetter.WordProcessingMerger_getFields(self)
    def getItems(self): return _NavalLetter.WordProcessingMerger_getItems(self)
    def getItemParent(self, *args): return _NavalLetter.WordProcessingMerger_getItemParent(self, *args)
    def getItemFields(self, *args): return _NavalLetter.WordProcessingMerger_getItemFields(self, *args)
    def setCodePage(self, *args): return _NavalLetter.WordProcessingMerger_setCodePage(self, *args)
    def setNumFracSep(self, p_frac=0): return _NavalLetter.WordProcessingMerger_setNumFracSep(self, p_frac)
    def setNumThSep(self, p_th=0): return _NavalLetter.WordProcessingMerger_setNumThSep(self, p_th)
    def setDateFormat(self, p_format=""): return _NavalLetter.WordProcessingMerger_setDateFormat(self, p_format)
    def setYearOffset(self, p_year=0): return _NavalLetter.WordProcessingMerger_setYearOffset(self, p_year)
    def setFirstWeekDay(self, *args): return _NavalLetter.WordProcessingMerger_setFirstWeekDay(self, *args)
    def setWeekDayNames(self, *args): return _NavalLetter.WordProcessingMerger_setWeekDayNames(self, *args)
    def setMonthNames(self, *args): return _NavalLetter.WordProcessingMerger_setMonthNames(self, *args)
    def getCodePage(self): return _NavalLetter.WordProcessingMerger_getCodePage(self)
    def getNumFracSep(self): return _NavalLetter.WordProcessingMerger_getNumFracSep(self)
    def getNumThSep(self): return _NavalLetter.WordProcessingMerger_getNumThSep(self)
    def getDateFormat(self): return _NavalLetter.WordProcessingMerger_getDateFormat(self)
    def getYearOffset(self): return _NavalLetter.WordProcessingMerger_getYearOffset(self)
    def getFirstWeekDay(self): return _NavalLetter.WordProcessingMerger_getFirstWeekDay(self)
    def getWeekDayFullNames(self): return _NavalLetter.WordProcessingMerger_getWeekDayFullNames(self)
    def getWeekDayShortNames(self): return _NavalLetter.WordProcessingMerger_getWeekDayShortNames(self)
    def getMonthFullNames(self): return _NavalLetter.WordProcessingMerger_getMonthFullNames(self)
    def getMonthShortNames(self): return _NavalLetter.WordProcessingMerger_getMonthShortNames(self)
    def setTempDir(self, *args): return _NavalLetter.WordProcessingMerger_setTempDir(self, *args)
    def getWorkDir(self): return _NavalLetter.WordProcessingMerger_getWorkDir(self)
    def getTempDir(self): return _NavalLetter.WordProcessingMerger_getTempDir(self)
WordProcessingMerger_swigregister = _NavalLetter.WordProcessingMerger_swigregister
WordProcessingMerger_swigregister(WordProcessingMerger)

def WordProcessingMerger_getInstance():
  return _NavalLetter.WordProcessingMerger_getInstance()
WordProcessingMerger_getInstance = _NavalLetter.WordProcessingMerger_getInstance

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _NavalLetter.StringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _NavalLetter.StringVector___nonzero__(self)
    def __bool__(self): return _NavalLetter.StringVector___bool__(self)
    def __len__(self): return _NavalLetter.StringVector___len__(self)
    def pop(self): return _NavalLetter.StringVector_pop(self)
    def __getslice__(self, *args): return _NavalLetter.StringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _NavalLetter.StringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _NavalLetter.StringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _NavalLetter.StringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _NavalLetter.StringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _NavalLetter.StringVector___setitem__(self, *args)
    def append(self, *args): return _NavalLetter.StringVector_append(self, *args)
    def empty(self): return _NavalLetter.StringVector_empty(self)
    def size(self): return _NavalLetter.StringVector_size(self)
    def clear(self): return _NavalLetter.StringVector_clear(self)
    def swap(self, *args): return _NavalLetter.StringVector_swap(self, *args)
    def get_allocator(self): return _NavalLetter.StringVector_get_allocator(self)
    def begin(self): return _NavalLetter.StringVector_begin(self)
    def end(self): return _NavalLetter.StringVector_end(self)
    def rbegin(self): return _NavalLetter.StringVector_rbegin(self)
    def rend(self): return _NavalLetter.StringVector_rend(self)
    def pop_back(self): return _NavalLetter.StringVector_pop_back(self)
    def erase(self, *args): return _NavalLetter.StringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _NavalLetter.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _NavalLetter.StringVector_push_back(self, *args)
    def front(self): return _NavalLetter.StringVector_front(self)
    def back(self): return _NavalLetter.StringVector_back(self)
    def assign(self, *args): return _NavalLetter.StringVector_assign(self, *args)
    def resize(self, *args): return _NavalLetter.StringVector_resize(self, *args)
    def insert(self, *args): return _NavalLetter.StringVector_insert(self, *args)
    def reserve(self, *args): return _NavalLetter.StringVector_reserve(self, *args)
    def capacity(self): return _NavalLetter.StringVector_capacity(self)
    __swig_destroy__ = _NavalLetter.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _NavalLetter.StringVector_swigregister
StringVector_swigregister(StringVector)


def initialize():
  return _NavalLetter.initialize()
initialize = _NavalLetter.initialize

def print_Reply(*args):
  return _NavalLetter.print_Reply(*args)
print_Reply = _NavalLetter.print_Reply

def print_Header(*args):
  return _NavalLetter.print_Header(*args)
print_Header = _NavalLetter.print_Header

def print_FromToSubj(*args):
  return _NavalLetter.print_FromToSubj(*args)
print_FromToSubj = _NavalLetter.print_FromToSubj

def print_Via(*args):
  return _NavalLetter.print_Via(*args)
print_Via = _NavalLetter.print_Via

def print_Ref(*args):
  return _NavalLetter.print_Ref(*args)
print_Ref = _NavalLetter.print_Ref

def print_Encl(*args):
  return _NavalLetter.print_Encl(*args)
print_Encl = _NavalLetter.print_Encl

def print_Body(*args):
  return _NavalLetter.print_Body(*args)
print_Body = _NavalLetter.print_Body

def print_Copy(*args):
  return _NavalLetter.print_Copy(*args)
print_Copy = _NavalLetter.print_Copy

def print_Sig(*args):
  return _NavalLetter.print_Sig(*args)
print_Sig = _NavalLetter.print_Sig

def save_Output(*args):
  return _NavalLetter.save_Output(*args)
save_Output = _NavalLetter.save_Output
# This file is compatible with both classic and new-style classes.



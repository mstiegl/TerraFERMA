import sys
import libspud
import buckettools.functionbucket

class SpudFunctionBucket(buckettools.functionbucket.FunctionBucket):
  """A class that stores all the information necessary to write the ufl for a function (field or coefficient) 
     plus all the information necessary to populate that class using libspud.
     Note that the class has limited ufl production because much of this is system dependent."""

  def fill(self, optionpath, system, index):
    """Fill a function class with data describing that function using libspud, the given optionpath and the system its based on."""
    self.name       = libspud.get_option(optionpath+"/name")
    self.symbol     = libspud.get_option(optionpath+"/ufl_symbol").split("\n")[0]
    self.system     = system
    self.index      = index
    self.type       = libspud.get_option(optionpath+"/type/name")

    self.rank   = libspud.get_option(optionpath+"/type/rank/name")
    self.family   = None
    self.degree = None
    self.functional = None
    if self.type != "Constant":
      self.family = libspud.get_option(optionpath+"/type/rank/element/family")
      self.degree = libspud.get_option(optionpath+"/type/rank/element/degree")

    self.size     = None
    self.shape    = None
    self.symmetry = None
    if self.rank == "Vector":
      if libspud.have_option(optionpath+"/type/rank/element/size"):
        self.size = libspud.get_option(optionpath+"/type/rank/element/size")
    elif self.rank == "Tensor":
      if libspud.have_option(optionpath+"/type/rank/element/shape"):
        self.shape = libspud.get_option(optionpath+"/type/rank/element/shape")
      if libspud.have_option(optionpath+"/type/rank/element/symmetry"):
        self.symmetry = True

    # this should be restricted by the schema to Constant coefficients:
    if libspud.have_option(optionpath+"/type/rank/value/functional"):
      functional_optionpath = optionpath+"/type/rank/value/functional"
      functional = buckettools.spud.SpudFunctionalBucket()
      functional.fill(functional_optionpath, self)
      self.functional = functional
    
    self.cpp = []
    for k in range(libspud.option_count(optionpath+"/type/rank/initial_condition")):
      cpp_optionpath = optionpath+"/type/rank/initial_condition["+`k`+"]"
      if libspud.have_option(cpp_optionpath+"/cpp"):
        cpp_name = libspud.get_option(cpp_optionpath+"/name")
        cppexpression = buckettools.spud.SpudCppExpressionBucket()
        # get all the information about this expression from the options dictionary
        cppexpression.fill(cpp_optionpath, cpp_name, self)
        # let the field know about this cpp expression
        self.cpp.append(cppexpression)
        # done with this expression
        del cppexpression

    for j in range(libspud.option_count(optionpath+"/type/rank/boundary_condition")):
      bc_optionpath = optionpath+"/type/rank/boundary_condition["+`j`+"]"
      bc_name = libspud.get_option(bc_optionpath+"/name")
      for k in range(libspud.option_count(bc_optionpath+"/sub_components")):
        bc_comp_optionpath = bc_optionpath+"/sub_components["+`k`+"]"
        bc_comp_name = libspud.get_option(bc_comp_optionpath+"/name")
        
        cpp_optionpath = bc_comp_optionpath+"/type"
        if libspud.have_option(cpp_optionpath+"/cpp"):
          cpp_name = bc_name + bc_comp_name
          
          cppexpression = buckettools.spud.SpudCppExpressionBucket()
          # get all the information about this expression from the options dictionary
          cppexpression.fill(cpp_optionpath, cpp_name, self)
          # let the field know about this cpp expression
          self.cpp.append(cppexpression)
          # done with this expression
          del cppexpression

    for k in range(libspud.option_count(optionpath+"/type/rank/value")):
      cpp_optionpath = optionpath+"/type/rank/value["+`k`+"]"
      if libspud.have_option(cpp_optionpath+"/cpp"):
        cpp_name = libspud.get_option(cpp_optionpath+"/name")
        cppexpression = buckettools.spud.SpudCppExpressionBucket()
        # get all the information about this expression from the options dictionary
        cppexpression.fill(cpp_optionpath, cpp_name, self)
        # let the field know about this cpp expression
        self.cpp.append(cppexpression)
        # done with this expression
        del cppexpression

    self.functionals = []
    for k in range(libspud.option_count(optionpath+"/diagnostics/include_in_statistics/functional")):
      functional_optionpath = optionpath+"/diagnostics/include_in_statistics/functional["+`k`+"]"
      functional = buckettools.spud.SpudFunctionalBucket()
      # get all the information about this functional from the options dictionary
      functional.fill(functional_optionpath, self)
      # let the field know about this functional
      self.functionals.append(functional)
      # done with this functional
      del functional

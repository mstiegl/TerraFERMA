
#ifndef __PYTHON_DETECTORS_H
#define __PYTHON_DETECTORS_H

#include "GenericDetectors.h"
#include <dolfin.h>
#include "PythonInstance.h"

namespace buckettools
{
  
  //*****************************************************************|************************************************************//
  // PythonDetectors class:
  //
  // PythonDetectors is a derived class of GenericDetectors that implements an array of detectors described by a python function
  //*****************************************************************|************************************************************//
  class PythonDetectors : public GenericDetectors
  {

  //*****************************************************************|***********************************************************//
  // Publicly available functions
  //*****************************************************************|***********************************************************//

  public:

    //***************************************************************|***********************************************************//
    // Constructors and destructors
    //***************************************************************|***********************************************************//

    PythonDetectors(const uint &number_detectors, 
                    const uint &meshdim, 
                    const std::string &function, 
                    const std::string &name);
    
    ~PythonDetectors();
    
    //***************************************************************|***********************************************************//
    // Output
    //***************************************************************|***********************************************************//

    const std::string str() const;                                 // return a string that describes the detectors 
    
  //*****************************************************************|***********************************************************//
  // Private functions
  //*****************************************************************|***********************************************************//

  private:
    
    //***************************************************************|***********************************************************//
    // Base data
    //***************************************************************|***********************************************************//

    PythonInstance pyinst_;                                          // an object that describes the base python function
    
    //***************************************************************|***********************************************************//
    // Initialization
    //***************************************************************|***********************************************************//

    void init_();                                                    // initialize the python detectors
    
  };
  
  typedef boost::shared_ptr< PythonDetectors > PythonDetectors_ptr;  // define a (boost shared) pointer for this class type
  
}

#endif

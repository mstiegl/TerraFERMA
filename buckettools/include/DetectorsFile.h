// Copyright (C) 2013 Columbia University in the City of New York and others.
//
// Please see the AUTHORS file in the main source directory for a full list
// of contributors.
//
// This file is part of TerraFERMA.
//
// TerraFERMA is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// TerraFERMA is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with TerraFERMA. If not, see <http://www.gnu.org/licenses/>.


#ifndef __DETECTORS_FILE_H
#define __DETECTORS_FILE_H

#include <cstdio>
#include <fstream>
#include <string>
#include <dolfin.h>
#include "DiagnosticsFile.h"
#include "BoostTypes.h"

namespace buckettools
{

  //*****************************************************************|************************************************************//
  // predeclarations: a circular dependency between the DetectorsFile class and the Bucket class requires a lot of predeclarations.
  //*****************************************************************|************************************************************//
  class Bucket;
  class SystemBucket;
  typedef std::shared_ptr< SystemBucket > SystemBucket_ptr;
  class FunctionBucket;
  typedef std::shared_ptr< FunctionBucket > FunctionBucket_ptr;
  class GenericDetectors;
  typedef std::shared_ptr< GenericDetectors > GenericDetectors_ptr;

  //*****************************************************************|************************************************************//
  // DetectorsFile class:
  //
  // A derived class from the base statfile class intended for the output of detectors data to file every dump period.
  //*****************************************************************|************************************************************//
  class DetectorsFile : public DiagnosticsFile
  {

  //*****************************************************************|***********************************************************//
  // Publicly available functions
  //*****************************************************************|***********************************************************//

  public:
    
    //***************************************************************|***********************************************************//
    // Constructors and destructors
    //***************************************************************|***********************************************************//
    
    DetectorsFile(const std::string name, 
                  const MPI_Comm &comm, 
                  const Bucket *bucket);     // specific constructor
    
    ~DetectorsFile();                                                // default destructor
    
    //***************************************************************|***********************************************************//
    // Header writing functions
    //***************************************************************|***********************************************************//

    void write_header();
    
    //***************************************************************|***********************************************************//
    // Data writing functions
    //***************************************************************|***********************************************************//

    void write_data();
    
  //*****************************************************************|***********************************************************//
  // Private functions
  //*****************************************************************|***********************************************************//

  private:
    
    //***************************************************************|***********************************************************//
    // Base data
    //***************************************************************|***********************************************************//

    std::vector< GenericDetectors_ptr > detectors_;

    std::vector< FunctionBucket_ptr >   functions_;

    //***************************************************************|***********************************************************//
    // Header writing functions (continued)
    //***************************************************************|***********************************************************//

    void header_bucket_();
    
    void header_detector_(const GenericDetectors_ptr d_ptr);
    
    void header_func_(const FunctionBucket_ptr f_ptr);
    
    //***************************************************************|***********************************************************//
    // Data writing functions (continued)
    //***************************************************************|***********************************************************//

    void data_timestep_();

    void data_bucket_();
    
    void data_detector_(const GenericDetectors_ptr d_ptr);
    
    void data_func_(const FunctionBucket_ptr f_ptr);

    //***************************************************************|***********************************************************//
    // Private members
    //***************************************************************|***********************************************************//

#ifdef HAS_MPI
    MPI_File mpifile_;

    MPI_Offset mpiwritelocation_;
#endif
    
    uint mpiwritecount_;

  };
  
  typedef std::shared_ptr< DetectorsFile > DetectorsFile_ptr;          // define a boost shared ptr type for the class

}
#endif

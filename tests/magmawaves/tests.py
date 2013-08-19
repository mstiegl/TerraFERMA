# Copyright (C) 2013 Columbia University in the City of New York and others.
#
# Please see the AUTHORS file in the main source directory for a full list
# of contributors.
#
# This file is part of TerraFERMA.
#
# TerraFERMA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TerraFERMA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with TerraFERMA. If not, see <http://www.gnu.org/licenses/>.

from buckettools.statfile import parser
import numpy
from math import sqrt

det = parser("magmawaves.det")
stat = parser("magmawaves.stat")

def test_Porosity_center():
  val = det["magma"]["Porosity"]["x0"][0,-1]
  test = 2.3359664311e+00
  assert abs(val - test) < 0.001
  print "\tvalue=", val, "test=", test, " ",

def test_Pressure_center():
  val = det["magma"]["Pressure"]["x0"][0,-1]
  test = 0
  assert abs(val - test) < 1.e-5
  print "\tvalue=", val, "test=", test, " ",

def test_Porosity_integral():
  val = stat["magma"]["Porosity"]["Integral"][-1]
  test = 1.0378229285e+00
  assert abs(val - test) < 0.00001
  print "\tvalue=", val, "test=", test, " ",

def test_Pressure_integral():
  val = stat["magma"]["Pressure"]["IntegralPressure"][-1]
  test = 0.
  assert abs(val - test) < 1.e-10
  print "\tvalue=", val, "test=", test, " ",

def test_Porosity_L2error():
  val = stat["magma"]["Porosity"]["L2error"][-1]
  val = sqrt(val)
  test = sqrt(1.4065673868e-8)
  assert abs(val - test) < 1.e-5
  print "\tvalue=", val, "test=", test, " ",
  
def test_timestep():
  val = stat["timestep"]["value"][-1]
  test = 1282
  assert abs(val - test) < 1
  print "\tvalue=", val, "test=", test, " ",

def test_walltime():
  val = stat["ElapsedWallTime"]["value"][-1]
  test = 600.
  assert abs(val) < test
  print "\tvalue=", val, "< ", test, " ",

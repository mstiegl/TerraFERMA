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

stat = parser("adaptdt.stat")

def test_mincourant():
  val = stat["CourantNumber"]["AltCourantNumber"]["min"][1:].min()
  assert numpy.all(val==10.)

def test_maxcourant():
  val = stat["CourantNumber"]["AltCourantNumber"]["max"][1:].max()
  assert numpy.all(val==15.0)

def test_dt():
  val = stat["dt"]["value"]
  expectedval = numpy.array([ 1.    ,  1.    ,  1.    , \
                              1.1   ,  1.1   ,  \
                              1.21  ,  1.21  ,  \
                              1.331 ,  1.331 ,  \
                              1.4641,  1.4641,  \
                              1.5   ,  1.5   ,  1.5   ,    1.5   ,  1.5   ,  1.5   ])
  assert numpy.all(abs(val-expectedval) < 1.e-14)


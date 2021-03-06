#! /usr/bin/env python3

# This file is a part of NUMCL project.
# Copyright (c) 2019 IBM Corporation
# SPDX-License-Identifier: LGPL-3.0-or-later
# 
# NUMCL is free software: you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any
# later version.
# 
# NUMCL is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# NUMCL.  If not, see <http://www.gnu.org/licenses/>.

from numpy import *
from benchmarker import Benchmarker, Reporter

class Short(Reporter):
    def __init__(self):
        super().__init__(20)
    def report_ranking(self, benchmarks):
        return ''
    def report_matrix(self, benchmarks):
        return ''

with Benchmarker(loop=100, filter="tag!=slow", reporter=Short()) as bench:

    a = zeros((10,10,10))
    b = zeros((10,10,10))

    @bench('4concat/concatenate/0')
    def run(bm):
        for i in bm:
            concatenate((a, b), axis=0)
    @bench('4concat/concatenate/1')
    def run(bm):
        for i in bm:
            concatenate((a, b), axis=1)
    @bench('4concat/concatenate/2')
    def run(bm):
        for i in bm:
            concatenate((a, b), axis=2)
    @bench('4concat/stack/0')
    def run(bm):
        for i in bm:
            stack((a, b), axis=0)
    @bench('4concat/stack/1')
    def run(bm):
        for i in bm:
            stack((a, b), axis=1)
    @bench('4concat/stack/2')
    def run(bm):
        for i in bm:
            stack((a, b), axis=2)
    # @bench('4concat/split/0')
    # def run(bm):
    #     for i in bm:
    #         split(a, axis=0)
    # @bench('4concat/split/1')
    # def run(bm):
    #     for i in bm:
    #         split(a, axis=1)
    # @bench('4concat/split/2')
    # def run(bm):
    #     for i in bm:
    #         split(a, axis=2)

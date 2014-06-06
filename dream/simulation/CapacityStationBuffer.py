# ===========================================================================
# Copyright 2013 University of Limerick
#
# This file is part of DREAM.
#
# DREAM is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DREAM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DREAM.  If not, see <http://www.gnu.org/licenses/>.
# ===========================================================================

'''
Created on 6 June 2013

@author: George
'''
'''
the buffer of the capacity station. Only change from queue that it can be blocked.
'''

import simpy
from Queue import Queue
# ===========================================================================
#                            the Queue object
# ===========================================================================
class CapacityStationBuffer(Queue):
    #===========================================================================
    # the __init__ method of the CapacityStationBuffer
    #===========================================================================
    def __init__(self, id, name, capacity=float("inf"), isDummy=False, schedulingRule="FIFO", gatherWipStat=False):
        Queue.__init__(self, id, name, capacity=capacity)
        self.isLocked=True


    def initialize(self):
        Queue.initialize(self)
        self.isLocked=True

    def canAccept(self, callerObject=None):
        if self.isLocked:
            return False
        return Queue.canAccept(self)

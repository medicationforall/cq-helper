# Copyright 2024 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cadquery as cq

#shamelessly yoinked from cqindustry
def jersey_shape(
    width:float = 10,
    height:float = 10,
    base_height:float = 2,
    middle_width_inset:float = -2,
    middle_height:float = 2,
    top_width_inset:float = -1
) -> cq.Workplane:
    mid_height = base_height + middle_height
    top_width = middle_width_inset + top_width_inset
    pts = [
        (0,0),
        (0,width),# base width
        (base_height,width),#base Height
        (mid_height, width + middle_width_inset), # middle

        (height,width + top_width),# top
        (height,-1*(top_width)),# top

        (mid_height, -1*(middle_width_inset)), # middle
        (base_height,0)
    ]

    result = (
        cq.Workplane("XY")
        .center(-1*(height/2),-1*(width/2))
        .polyline(pts)
        .close()
    )
    return result

def jersey_barrier(
    length:float = 75,
    width:float = 20,
    height:float = 25,
    base_height:float = 4,
    middle_width_inset:float = -4,
    middle_height:float = 2,
    top_width_inset:float = -1
) -> cq.Workplane:
    j_barrier = jersey_shape(
        width,
        height,
        base_height,
        middle_width_inset,
        middle_height,
        top_width_inset
    )
    
    if length:
        j_barrier = j_barrier.extrude(length)
        return (
            j_barrier
            .translate((0,0,-(length/2)))
            .rotate((0,1,0),(0,0,0),90)
        )
    else:
        return j_barrier

    
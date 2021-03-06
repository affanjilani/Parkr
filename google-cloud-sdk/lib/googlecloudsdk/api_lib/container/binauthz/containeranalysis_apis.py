# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""API helpers for the interacting with binauthz."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base

V1_BETA1 = 'v1beta1'
V1 = 'v1'


def GetApiVersion(release_track):
  # TODO(b/138859339): Migrate GA and beta commands to containeranalysis v1.
  if release_track == base.ReleaseTrack.GA:
    return V1_BETA1
  elif release_track == base.ReleaseTrack.BETA:
    return V1_BETA1
  elif release_track == base.ReleaseTrack.ALPHA:
    return V1
  else:
    raise ValueError('Unsupported Release Track: {}'.format(release_track))

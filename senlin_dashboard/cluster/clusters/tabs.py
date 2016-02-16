# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from senlin_dashboard.api import senlin
from senlin_dashboard.cluster.nodes import tabs as node_tab


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = ("cluster/clusters/_detail_overview.html")

    def get_context_data(self, request):
        return {"cluster": self.tab_group.kwargs['cluster']}


class EventTab(node_tab.EventTab):

    def get_event_data(self):
        cluster_id = self.tab_group.kwargs['cluster_id']
        try:
            params = {"obj_id": cluster_id}
            events = senlin.event_list(self.request, params)
        except Exception:
            events = []
            exceptions.handle(self.request,
                              _('Unable to retrieve cluster event list.'))
        return sorted(events, reverse=True, key=lambda y: y.timestamp)


class ClusterDetailTabs(tabs.TabGroup):
    slug = "cluster_details"
    tabs = (OverviewTab, EventTab)

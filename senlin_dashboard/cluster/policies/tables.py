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

from horizon import tables
from horizon.utils import filters


class PoliciesTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    type = tables.Column("type", verbose_name=_("Type"))
    spec = tables.Column("spec", verbose_name=_("Spec"))
    level = tables.Column("level", verbose_name=_("Level"))
    cooldown = tables.Column("cooldown", verbose_name=_("Cooldown"))
    created = tables.Column(
        "created_time",
        verbose_name=_("Created"),
        filters=(
            filters.parse_isotime,
            filters.timesince_or_never
        )
    )
    updated = tables.Column(
        "updated_time",
        verbose_name=_("Updated"),
        filters=(
            filters.parse_isotime,
            filters.timesince_or_never
        )
    )

    class Meta(object):
        name = "policies"
        verbose_name = _("Policies")
        table_actions = (tables.FilterAction,)
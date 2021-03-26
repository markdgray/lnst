from lnst.Controller import Controller, HostReq, DeviceReq, BaseRecipe
from lnst.Recipes.ENRT import NoVirtOvsVxlanRecipe

from lnst.Controller.RunSummaryFormatter import RunSummaryFormatter
from lnst.Controller.RecipeResults import ResultLevel

import logging

ctl = Controller(debug=1)
recipe_instance = NoVirtOvsVxlanRecipe(driver="lnst", perf_tests=["tcp_stream", "udp_stream"],perf_duration=300, perf_msg_sizes=[16384], mtu=1450)
ctl.run(recipe_instance)


summary_fmt = RunSummaryFormatter(
    level=ResultLevel.IMPORTANT + 0, colourize=True
)
for run in recipe_instance.runs:
    logging.info(summary_fmt.format_run(run))

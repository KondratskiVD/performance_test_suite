from queue import Empty
from sqlalchemy import and_

from pylon.core.tools import web, log  # pylint: disable=E0611,E0401
from tools import auth  # pylint: disable=E0401


class Slot:  # pylint: disable=E1101,R0903
    @web.slot('performance_test_suite_content')
    # @auth.decorators.check_slot({
    #     "permissions": ["performance.suite"]
    # })
    def content(self, context, slot, payload):
        project_id = context.rpc_manager.call.project_get_id()
        # public_regions = context.rpc_manager.call.get_rabbit_queues("carrier", True)
        # runners_query = Runner.query.with_entities(
        #     Runner.container_type, Runner.config
        # ).filter(
        #     and_(Runner.project_id == project_id, Runner.is_active == True)
        # ).all()
        # if runners_query:
        #     runners = {}
        #     for container_type, config in runners_query:
        #         runners.setdefault(container_type, {}).update(config)
        #     jmeter_runners = list(map(lambda i: {'version': i}, runners['jmeter'].keys()))
        #     gatling_runners = list(map(lambda i: {'version': i}, runners['gatling'].keys()))
        #     executable_runners = list(
        #         map(lambda i: {'version': i}, runners['executable_jar'].keys()))
        # else:
        #     jmeter_runners = list(map(lambda i: {'version': i}, JMETER_MAPPING.keys()))
        #     gatling_runners = list(map(lambda i: {'version': i}, GATLING_MAPPING.keys()))
        #     executable_runners = list(map(lambda i: {'version': i}, EXECUTABLE_MAPPING.keys()))
        # project_regions = context.rpc_manager.call.get_rabbit_queues(
        #     f"project_{project_id}_vhost")
        # try:
        #     cloud_regions = context.rpc_manager.timeout(3).integrations_get_cloud_integrations(
        #         project_id)
        # except Empty:
        #     cloud_regions = []
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance_test_suite/content.html',
            )

    @web.slot('backend_performance_scripts')
    def scripts(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance_test_suite/scripts.html',
            )

    @web.slot('backend_performance_styles')
    def styles(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance_test_suite/styles.html',
            )

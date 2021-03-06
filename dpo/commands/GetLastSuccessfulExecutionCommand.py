from dpo.commands.BaseCommand import BaseCommand
from dpo.Shared import Constants


class GetLastSuccessfulExecutionCommand(BaseCommand):
    def __init__(self, db_connection_string, logger=None):
        super().__init__(db_connection_string, logger)

    def execute(self):
        data_pipeline_execution = self.repository.get_last_successful_execution()
        self.logger.debug('Found last successful data_pipeline_execution to be ' + str(data_pipeline_execution))
        self.output(data_pipeline_execution)

    def output(self, data_pipeline_execution):
        print(str(data_pipeline_execution.execution_id) if data_pipeline_execution is not None
              else Constants.NO_LAST_SUCCESSFUL_EXECUTION)

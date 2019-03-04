from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from mcd.Shared import Constants
from mcd import Shared

TABLE_NAME = 'data_pipeline_execution'
PRIMARY_KEY_COL_NAME = 'id'


class DataPipelineExecutionEntity(Shared.BaseEntity):

    __tablename__ = TABLE_NAME
    __table_args__ = {'schema': Constants.DATA_PIPELINE_EXECUTION_SCHEMA_NAME}

    id = Column(PRIMARY_KEY_COL_NAME,
                UUID(as_uuid=True),
                primary_key=True,
                default=uuid.uuid4())

    created_on = Column('created_on',
                        DateTime(timezone=True),
                        nullable=False,
                        server_default=func.now())

    last_updated_on = Column('last_updated_on',
                             DateTime(timezone=True),
                             nullable=False,
                             server_default=func.now(),
                             onupdate=func.now())

    # unused for now, for future use
    execution_time_ms = Column('execution_time_ms',
                               Integer,
                               nullable=True)

    status = Column('status',
                    String(50),
                    nullable=False,
                    server_default=str(Constants.DataPipelineExecutionStatus.INITIALISED))

    def __str__(self):
        return f'id={self.id}, ' \
               f'created_on={self.created_on}, ' \
               f'last_updated_on={self.last_updated_on}, ' \
               f'execution_time_ms={self.execution_time_ms}, ' \
               f'status={self.status}.'

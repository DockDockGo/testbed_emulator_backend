from enum import Enum

FLEET_INFRA_IP_AND_PORT = "0.0.0.0:5001"

# A work cell is a physical location in the factory where a robot can be assigned to perform a task
class WorkCell(Enum):
    UNDEFINED = 0
    STOCK_ROOM = 3
    KITTING_STATION = 6
    ASSEMBLY_STATION = 1
    QA_STATION = 2


class TaskStatus(Enum):
    BACKLOG = 1
    ENQUEUED = 2
    RUNNING = 3
    COMPLETED = 4
    FAILED = 5
    CANCELED = 6


# An AMR is an autonomous mobile robot. We currently have the following 2 robots at the testbed
class AMR(Enum):
    RICK = 1
    MORTY = 2


ASSEMBLY_WORKFLOW_PRESET = {
    'fetch_parts_bins': {
        'workcell_id': WorkCell.STOCK_ROOM.value,
        'status': TaskStatus.BACKLOG.value,
    },
    'transport_parts_bins_to_kitting_station': {
        'navigate_to_source_subtask': {
            'amr_id': None,
            'start': WorkCell.UNDEFINED.value,
            'goal': WorkCell.STOCK_ROOM.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'loading_subtask': {
            'workcell_id': WorkCell.STOCK_ROOM.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'navigate_to_sink_subtask': {
            'amr_id': None,
            'start': WorkCell.STOCK_ROOM.value,
            'goal': WorkCell.KITTING_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'unloading_subtask': {
            'workcell_id': WorkCell.KITTING_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
    },
    'kitting_task': {
        'workcell_id': WorkCell.KITTING_STATION.value,
        'status': TaskStatus.BACKLOG.value,
    },
    'transport_kitting_task_payload_to_assembly_station': {
        'navigate_to_source_subtask': {
            'amr_id': None,
            'start': WorkCell.UNDEFINED.value,
            'goal': WorkCell.KITTING_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'loading_subtask': {
            'workcell_id': WorkCell.KITTING_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'navigate_to_sink_subtask': {
            'amr_id': None,
            'start': WorkCell.KITTING_STATION.value,
            'goal': WorkCell.ASSEMBLY_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'unloading_subtask': {
            'workcell_id': WorkCell.ASSEMBLY_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
    },
    'assembly_task': {
        'workcell_id': WorkCell.ASSEMBLY_STATION.value,
        'status': TaskStatus.BACKLOG.value,
    },
    'transport_assembly_task_payload_to_qa_station': {
        'navigate_to_source_subtask': {
            'amr_id': None,
            'start': WorkCell.UNDEFINED.value,
            'goal': WorkCell.ASSEMBLY_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'loading_subtask': {
            'workcell_id': WorkCell.ASSEMBLY_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'navigate_to_sink_subtask': {
            'amr_id': None,
            'start': WorkCell.ASSEMBLY_STATION.value,
            'goal': WorkCell.QA_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
        'unloading_subtask': {
            'workcell_id': WorkCell.QA_STATION.value,
            'status': TaskStatus.BACKLOG.value,
        },
    },
}

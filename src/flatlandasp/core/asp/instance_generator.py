import inspect
from typing import Tuple

from flatland.envs.rail_env import RailEnv

from flatlandasp.core.asp.errors.instance_not_found_error import \
    InstanceNotFoundError
from flatlandasp.core.asp.errors.rails_not_found_error import \
    RailsNotFoundError
from flatlandasp.core.asp.instance_description import InstanceDescription
from flatlandasp.core.flatland.mappings import \
    CELL_ID_TO_TYPE_AND_ORIENTATON_MAP
from flatlandasp.core.flatland.schemas.agent import Agent
from flatlandasp.core.flatland.schemas.cell import Cell
from flatlandasp.core.flatland.schemas.cell_type import CellType
from flatlandasp.core.flatland.schemas.orientation import Orientation
from flatlandasp.core.flatland.schemas.position import Position
from flatlandasp.core.utils.file_utils import write_lines_to_file_in_output


class InstanceGenerator:
    def __init__(self, *, instance_description: InstanceDescription) -> None:
        self.instance_description = instance_description
        self.instance = None

    def generate_instance_for_environment(self, *, env: RailEnv, step_limit: int = 100):
        cells, cell_types = self._get_cells_and_types_from_environment(env)
        agents = self._get_agents_from_environment(env)

        instance = [
            f'step_limit({step_limit}).',
            *self.instance_description.get_full_description(
                cells=cells,
                cell_types=list(cell_types),
                agents=agents
            )
        ]

        self.instance = instance

    def generate_instance_header(self) -> list[str]:
        header = inspect.cleandoc(
            f"""% This file was generated by the ASP instance generator.
                % Altering this file may interfere with results.
                %
                % Used instance description: {self.instance_description.__class__.__name__}
                \
            """
        ).splitlines()
        return header

    def store_instance(self, path, instance_name: str):
        if self.instance is None:
            raise InstanceNotFoundError()

        lines = [*self.generate_instance_header(), *self.instance]

        write_lines_to_file_in_output(
            path=path, file_name=f'{instance_name}.lp', lines=lines)

    def _get_agents_from_environment(self, env: RailEnv) -> list[Agent]:
        agents = []
        for i, agent in enumerate(env.agents):
            agents.append(
                Agent(
                    id=i,
                    position=Position(
                        x=agent.initial_position[1],
                        y=agent.initial_position[0]
                    ),
                    orientation=Orientation(int(agent.direction)),
                    target=Position(
                        x=agent.target[1],
                        y=agent.target[0]
                    ),
                    earliest_departure=agent.earliest_departure
                )
            )

        return agents

    def _get_cells_and_types_from_environment(self, env: RailEnv, *, ignore_empty_cells: bool = True) -> Tuple[list[Cell], set[CellType]]:
        if env.rail is None:
            raise RailsNotFoundError()

        cells: list[Cell] = []
        cell_types: set[CellType] = set()
        for y, row in enumerate(env.rail.grid):
            for x, column in enumerate(row):
                if ignore_empty_cells and column == 0:
                    continue
                cell_type, orientation = CELL_ID_TO_TYPE_AND_ORIENTATON_MAP[column]
                cell_types.add(cell_type)
                cell = Cell(type=cell_type,
                            orientation=orientation,
                            position=Position(x=x, y=y))
                cells.append(cell)

        return (cells, cell_types)

from abc import ABC, abstractmethod


class Agent(ABC):
    """
    Base interface for all autonomous agents in the system.

    An agent:
    - observes shared system state
    - decides independently when it can act
    - mutates shared state when acting

    Agents do NOT:
    - call other agents
    - know execution order
    - control orchestration
    """

    @abstractmethod
    def can_act(self, state) -> bool:
        """
        Determines whether the agent should act
        based on the current system state.

        Returns:
            bool: True if the agent can act, False otherwise
        """
        pass

    @abstractmethod
    def act(self, state) -> None:
        """
        Performs the agent's responsibility and
        updates the shared system state.

        This method should be side-effect free
        outside of state mutation.
        """
        pass

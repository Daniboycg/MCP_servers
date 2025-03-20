import { WorkflowSpec, WorkflowNode, WorkflowConnection } from '../types/workflow';
import { calculateNextPosition } from '../utils/positioning';

export class WorkflowBuilder {
  private nodes: WorkflowNode[] = [];
  private connections: WorkflowConnection[] = [];
  private nextPosition = { x: 100, y: 100 };

  addNode(node: WorkflowNode): WorkflowNode {
    if (!node.position) {
      node.position = { ...this.nextPosition };
      this.nextPosition = calculateNextPosition(this.nextPosition);
    }
    this.nodes.push(node);
    return node;
  }

  connectNodes(connection: WorkflowConnection) {
    this.connections.push(connection);
  }

  exportWorkflow(): WorkflowSpec {
    return {
      nodes: this.nodes,
      connections: this.connections
    };
  }
}

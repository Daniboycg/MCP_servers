export interface WorkflowNode {
  id?: string;
  type: string;
  name: string;
  parameters?: Record<string, any>;
  position?: { x: number; y: number };
}

export interface WorkflowConnection {
  source: string;
  target: string;
  sourceOutput?: number;
  targetInput?: number;
}

export interface WorkflowSpec {
  name?: string;
  nodes: WorkflowNode[];
  connections?: WorkflowConnection[];
  active?: boolean;
  settings?: Record<string, any>;
  tags?: string[];
}

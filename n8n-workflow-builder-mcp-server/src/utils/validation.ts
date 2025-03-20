import { WorkflowSpec } from '../types/workflow';
import { McpError, ErrorCode } from '@modelcontextprotocol/sdk/types.js';

export function validateWorkflowSpec(input: any): WorkflowSpec {
  if (!input || typeof input !== 'object') {
    throw new McpError(ErrorCode.InvalidParams, 'Workflow spec must be an object');
  }
  
  if (!Array.isArray(input.nodes)) {
    throw new McpError(ErrorCode.InvalidParams, 'Workflow nodes must be an array');
  }
  
  for (const node of input.nodes) {
    if (typeof node !== 'object' || typeof node.type !== 'string' || typeof node.name !== 'string') {
      throw new McpError(ErrorCode.InvalidParams, 'Each node must have a type and name');
    }
  }
  
  // If connections are provided, they must be an array.
  if (input.connections && !Array.isArray(input.connections)) {
    throw new McpError(ErrorCode.InvalidParams, 'Workflow connections must be an array');
  }
  
  // Return the validated workflow spec
  return {
    name: input.name,
    nodes: input.nodes,
    connections: input.connections || [],
    active: input.active,
    settings: input.settings,
    tags: input.tags
  };
}

import axios from 'axios';
import { N8N_HOST, N8N_API_KEY, GITHUB_TOKEN } from '../config/constants';
import { WorkflowSpec } from '../types/workflow';
import { ExecutionListOptions } from '../types/execution';
import { N8NWorkflowResponse, N8NExecutionResponse, N8NExecutionListResponse, NodeInfo, NodeListResponse } from '../types/api';

const api = axios.create({
  baseURL: N8N_HOST,
  headers: {
    'Content-Type': 'application/json',
    'X-N8N-API-KEY': N8N_API_KEY
  }
});

// GitHub API client with optional token for higher rate limits
const githubApi = axios.create({
  baseURL: 'https://api.github.com',
  headers: {
    'Accept': 'application/vnd.github.v3+json',
    ...(GITHUB_TOKEN ? { 'Authorization': `token ${GITHUB_TOKEN}` } : {})
  }
});

// Log the API configuration for debugging
console.log('N8N API Configuration:');
console.log('Host:', N8N_HOST);
console.log('API Key:', N8N_API_KEY ? '****' + N8N_API_KEY.slice(-4) : 'Not set');

/**
 * Helper function to handle API errors consistently
 * @param context Description of the operation that failed
 * @param error The error that was thrown
 */
function handleApiError(context: string, error: unknown): never {
  console.error(`Error ${context}:`, error);
  if (axios.isAxiosError(error)) {
    console.error('Request URL:', error.config?.url);
    console.error('Response status:', error.response?.status);
    console.error('Response data:', error.response?.data);
  }
  throw error;
}

/**
 * Helper function to build a URL with query parameters
 * @param basePath The base API path
 * @param params An object containing the query parameters
 * @returns The complete URL with query parameters
 */
function buildUrl(basePath: string, params: Record<string, any> = {}): string {
  const urlParams = new URLSearchParams();
  
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined) {
      urlParams.append(key, value.toString());
    }
  }
  
  const queryString = urlParams.toString();
  return `${basePath}${queryString ? '?' + queryString : ''}`;
}

export async function createWorkflow(workflow: WorkflowSpec): Promise<N8NWorkflowResponse> {
  try {
    console.log('Creating workflow');
    const response = await api.post('/workflows', workflow);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError('creating workflow', error);
  }
}

export async function getWorkflow(id: string): Promise<N8NWorkflowResponse> {
  try {
    console.log(`Getting workflow with ID: ${id}`);
    const response = await api.get(`/workflows/${id}`);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`getting workflow with ID ${id}`, error);
  }
}

export async function updateWorkflow(id: string, workflow: WorkflowSpec): Promise<N8NWorkflowResponse> {
  try {
    console.log(`Updating workflow with ID: ${id}`);
    const response = await api.put(`/workflows/${id}`, workflow);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`updating workflow with ID ${id}`, error);
  }
}

export async function deleteWorkflow(id: string): Promise<any> {
  try {
    console.log(`Deleting workflow with ID: ${id}`);
    const response = await api.delete(`/workflows/${id}`);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`deleting workflow with ID ${id}`, error);
  }
}

export async function activateWorkflow(id: string): Promise<N8NWorkflowResponse> {
  try {
    console.log(`Activating workflow with ID: ${id}`);
    const response = await api.patch(`/workflows/${id}/activate`, {});
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`activating workflow with ID ${id}`, error);
  }
}

export async function deactivateWorkflow(id: string): Promise<N8NWorkflowResponse> {
  try {
    console.log(`Deactivating workflow with ID: ${id}`);
    const response = await api.patch(`/workflows/${id}/deactivate`, {});
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`deactivating workflow with ID ${id}`, error);
  }
}

export async function listWorkflows(): Promise<N8NWorkflowResponse[]> {
  try {
    console.log('Listing workflows from:', `${N8N_HOST}`);
    const response = await api.get('/workflows');
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError('listing workflows', error);
  }
}

// Execution API Methods

/**
 * List workflow executions with optional filtering
 * 
 * @param options Filtering and pagination options
 * @returns A paginated list of executions
 * 
 * Pagination: This endpoint uses cursor-based pagination. To retrieve the next page:
 * 1. Check if the response contains a nextCursor property
 * 2. If present, use it in the next request as the cursor parameter
 * 3. Continue until nextCursor is no longer returned
 */
export async function listExecutions(options: ExecutionListOptions = {}): Promise<N8NExecutionListResponse> {
  try {
    console.log('Listing executions');
    
    const url = buildUrl('/executions', options);
    
    console.log(`Fetching executions from: ${url}`);
    const response = await api.get(url);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError('listing executions', error);
  }
}

/**
 * Get details of a specific execution
 * 
 * @param id The execution ID to retrieve
 * @param includeData Whether to include the full execution data (may be large)
 * @returns The execution details
 */
export async function getExecution(id: number, includeData?: boolean): Promise<N8NExecutionResponse> {
  try {
    console.log(`Getting execution with ID: ${id}`);
    const url = buildUrl(`/executions/${id}`, includeData ? { includeData: true } : {});
    const response = await api.get(url);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`getting execution with ID ${id}`, error);
  }
}

/**
 * Delete an execution by ID
 * 
 * @param id The execution ID to delete
 * @returns The response from the deletion operation
 */
export async function deleteExecution(id: number): Promise<N8NExecutionResponse> {
  try {
    console.log(`Deleting execution with ID: ${id}`);
    const response = await api.delete(`/executions/${id}`);
    console.log('Response:', response.status, response.statusText);
    return response.data;
  } catch (error) {
    return handleApiError(`deleting execution with ID ${id}`, error);
  }
}

/**
 * GitHub API methods for fetching n8n node information
 */

/**
 * List all available node directories from the n8n GitHub repository
 */
export async function listNodeDirectories(): Promise<string[]> {
  try {
    console.log('Listing node directories from GitHub');
    const response = await githubApi.get('/repos/n8n-io/n8n/contents/packages/nodes-base/nodes');
    
    // Filter only directories
    const directories = response.data
      .filter((item: any) => item.type === 'dir')
      .map((dir: any) => dir.name);
    
    return directories;
  } catch (error) {
    return handleApiError('listing node directories from GitHub', error);
  }
}

/**
 * Get information about an n8n node from GitHub
 * @param nodeName The name of the node directory
 */
export async function getNodeInfo(nodeName: string): Promise<NodeInfo> {
  try {
    console.log(`Getting node info for ${nodeName}`);
    
    // Path to the node's directory in the repository
    const nodePath = `packages/nodes-base/nodes/${nodeName}`;
    
    // Get the readme content if available
    let readmeContent: string | undefined;
    let readmePath: string | undefined;
    
    try {
      // Check for README.md file
      const readmeResponse = await githubApi.get(`/repos/n8n-io/n8n/contents/${nodePath}/README.md`);
      readmePath = readmeResponse.data.path;
      
      // Readme content is base64 encoded
      const encodedContent = readmeResponse.data.content;
      readmeContent = Buffer.from(encodedContent, 'base64').toString('utf-8');
    } catch (error) {
      console.warn(`No README.md found for node ${nodeName}`);
    }
    
    // Prepare node information
    const nodeInfo: NodeInfo = {
      name: nodeName,
      displayName: nodeName
        .replace(/-/g, ' ')
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase()),
      description: extractDescriptionFromReadme(readmeContent) || `n8n node for ${nodeName}`,
      documentationUrl: `https://github.com/n8n-io/n8n/tree/master/${nodePath}`,
      readmePath,
      readmeContent
    };
    
    return nodeInfo;
  } catch (error) {
    return handleApiError(`getting node info for ${nodeName}`, error);
  }
}

/**
 * List all available n8n nodes with basic information
 */
export async function listNodes(): Promise<NodeListResponse> {
  try {
    console.log('Listing all n8n nodes from GitHub');
    
    // Get all node directories
    const nodeDirectories = await listNodeDirectories();
    
    // Basic node information without readme content to keep the response size manageable
    const nodes: NodeInfo[] = nodeDirectories.map(dir => ({
      name: dir,
      displayName: dir
        .replace(/-/g, ' ')
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase()),
      description: `n8n node for ${dir}`,
      documentationUrl: `https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/${dir}`
    }));
    
    return { nodes };
  } catch (error) {
    return handleApiError('listing n8n nodes', error);
  }
}

/**
 * Helper function to extract a description from the README content
 */
function extractDescriptionFromReadme(content?: string): string | undefined {
  if (!content) return undefined;
  
  // Try to extract the first paragraph after the title
  const lines = content.split('\n');
  
  // Skip the title and empty lines
  let i = 0;
  while (i < lines.length && (lines[i].startsWith('#') || lines[i].trim() === '')) {
    i++;
  }
  
  // Collect the first paragraph
  let description = '';
  while (i < lines.length && lines[i].trim() !== '') {
    description += lines[i] + ' ';
    i++;
  }
  
  return description.trim();
}

# CLAUDE.md - AI Assistant Guide for geofold-fusion

## Project Overview

**Project Name:** geofold-fusion
**Status:** Initial Setup
**Purpose:** [To be defined - appears to be a project related to geospatial data fusion or geometric folding operations]

This document serves as a comprehensive guide for AI assistants (like Claude) working on this codebase. It outlines the project structure, development workflows, conventions, and best practices to follow.

---

## Table of Contents

1. [Codebase Structure](#codebase-structure)
2. [Development Workflow](#development-workflow)
3. [Technology Stack](#technology-stack)
4. [Key Conventions](#key-conventions)
5. [Git Workflow](#git-workflow)
6. [Testing Strategy](#testing-strategy)
7. [Common Tasks](#common-tasks)
8. [Architecture Patterns](#architecture-patterns)
9. [Code Style Guidelines](#code-style-guidelines)
10. [AI Assistant Specific Guidelines](#ai-assistant-specific-guidelines)

---

## Codebase Structure

### Current Structure
```
geofold-fusion/
├── .git/                 # Git repository metadata
└── CLAUDE.md            # This file - AI assistant guide
```

### Planned/Expected Structure
```
geofold-fusion/
├── src/                 # Source code
│   ├── core/           # Core business logic
│   ├── utils/          # Utility functions and helpers
│   ├── services/       # External service integrations
│   ├── models/         # Data models and types
│   └── index.ts        # Main entry point
├── tests/              # Test files
│   ├── unit/          # Unit tests
│   ├── integration/   # Integration tests
│   └── e2e/           # End-to-end tests
├── docs/              # Documentation
├── config/            # Configuration files
├── scripts/           # Build and utility scripts
├── .github/           # GitHub workflows and templates
├── package.json       # Project dependencies and scripts
├── tsconfig.json      # TypeScript configuration
├── .gitignore         # Git ignore patterns
├── README.md          # Project documentation
└── CLAUDE.md          # This AI assistant guide
```

**Note:** As the project evolves, update this structure to reflect the actual organization.

---

## Development Workflow

### Setting Up Development Environment

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd geofold-fusion
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   # or
   pnpm install
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with appropriate values
   ```

4. **Run development server:**
   ```bash
   npm run dev
   ```

### Development Cycle

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and test:**
   - Write code following project conventions
   - Add/update tests as needed
   - Run tests locally before committing

3. **Commit changes:**
   ```bash
   git add .
   git commit -m "feat: descriptive commit message"
   ```

4. **Push and create PR:**
   ```bash
   git push -u origin feature/your-feature-name
   ```

---

## Technology Stack

### Core Technologies
**Status:** To be determined based on project requirements

**Suggested Stack:**
- **Language:** TypeScript/JavaScript, Python, or Go (TBD)
- **Runtime:** Node.js, Python 3.x, or Go runtime
- **Package Manager:** npm, yarn, pnpm, pip, or go modules
- **Build Tool:** esbuild, webpack, or native tooling
- **Testing:** Jest, pytest, or Go testing framework

**Update this section once the technology stack is decided.**

---

## Key Conventions

### File Naming
- Use lowercase with hyphens for directories: `geofold-fusion/src/data-processing/`
- Use camelCase for TypeScript/JavaScript files: `dataProcessor.ts`
- Use PascalCase for React components: `DataVisualizer.tsx`
- Use snake_case for Python files: `data_processor.py`
- Test files should match source files with `.test` or `.spec` suffix: `dataProcessor.test.ts`

### Code Organization
- **One responsibility per file:** Each module should have a single, well-defined purpose
- **Export structure:** Use named exports for utilities, default exports for components/classes
- **Imports order:**
  1. External dependencies (third-party libraries)
  2. Internal absolute imports (from `src/`)
  3. Relative imports (from `./` or `../`)
  4. Type imports (if using TypeScript)

### Naming Conventions
- **Variables/Functions:** camelCase - `getUserData()`, `isValidInput`
- **Constants:** UPPER_SNAKE_CASE - `MAX_RETRY_ATTEMPTS`, `API_BASE_URL`
- **Classes/Types:** PascalCase - `DataProcessor`, `UserConfig`
- **Interfaces (TypeScript):** PascalCase with 'I' prefix optional - `UserInterface` or `IUser`
- **Private members:** Prefix with underscore - `_privateMethod()`, `_internalState`

---

## Git Workflow

### Branch Naming
- **Feature branches:** `feature/description` or `feat/description`
- **Bug fixes:** `fix/description` or `bugfix/description`
- **Hotfixes:** `hotfix/description`
- **Refactoring:** `refactor/description`
- **Documentation:** `docs/description`
- **Claude branches:** `claude/description-{sessionId}` (for AI-generated work)

### Commit Message Format
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

**Examples:**
```
feat(auth): add user authentication module

fix(api): resolve timeout issue in data fetch
refactor(utils): simplify error handling logic

test(core): add unit tests for data processor
```

### Pull Request Guidelines
1. **Title:** Clear and descriptive, following commit message format
2. **Description:** Include:
   - What changes were made and why
   - Any breaking changes
   - Testing performed
   - Screenshots/demos (if applicable)
3. **Review:** At least one approval required (when team is established)
4. **CI/CD:** All checks must pass before merging

---

## Testing Strategy

### Test Coverage Goals
- **Unit tests:** Aim for >80% code coverage
- **Integration tests:** Cover critical workflows
- **E2E tests:** Cover main user journeys

### Testing Principles
1. **Write tests first (TDD)** when adding new features
2. **Test behavior, not implementation** - focus on what the code does, not how
3. **Keep tests independent** - each test should run in isolation
4. **Use meaningful test names** - describe what is being tested and expected outcome
5. **Mock external dependencies** - use mocks/stubs for APIs, databases, etc.

### Running Tests
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test -- path/to/test/file.test.ts
```

---

## Common Tasks

### Adding a New Feature
1. Create feature branch: `git checkout -b feature/new-feature`
2. Plan the implementation (consider using TODO comments or task tracking)
3. Implement core functionality in `src/`
4. Add corresponding tests in `tests/`
5. Update documentation if needed
6. Run tests and linting
7. Commit and push changes
8. Create pull request

### Fixing a Bug
1. Create bug fix branch: `git checkout -b fix/bug-description`
2. Write a failing test that reproduces the bug
3. Fix the bug
4. Verify the test now passes
5. Run full test suite
6. Commit with descriptive message
7. Create pull request

### Updating Dependencies
```bash
# Check for outdated packages
npm outdated

# Update specific package
npm update package-name

# Update all packages (use with caution)
npm update

# Audit for security vulnerabilities
npm audit
npm audit fix
```

---

## Architecture Patterns

### Recommended Patterns

#### 1. **Separation of Concerns**
- Keep business logic separate from presentation
- Isolate external dependencies (APIs, databases)
- Use dependency injection where appropriate

#### 2. **Error Handling**
- Use try-catch blocks for async operations
- Implement custom error classes for different error types
- Always provide meaningful error messages
- Log errors appropriately (but don't expose sensitive data)

```typescript
// Example error handling pattern
class DataProcessingError extends Error {
  constructor(message: string, public code: string) {
    super(message);
    this.name = 'DataProcessingError';
  }
}

async function processData(data: unknown): Promise<Result> {
  try {
    // Processing logic
    return result;
  } catch (error) {
    if (error instanceof ValidationError) {
      throw new DataProcessingError('Invalid input data', 'INVALID_INPUT');
    }
    throw new DataProcessingError('Processing failed', 'PROCESSING_ERROR');
  }
}
```

#### 3. **Configuration Management**
- Use environment variables for environment-specific config
- Never commit secrets or API keys
- Provide `.env.example` with placeholder values
- Use a config module to centralize configuration access

#### 4. **Modular Design**
- Break down complex functionality into smaller modules
- Each module should have a clear, single responsibility
- Use interfaces/types to define contracts between modules
- Favor composition over inheritance

---

## Code Style Guidelines

### General Principles
1. **Readability over cleverness** - write code that others can easily understand
2. **Consistency** - follow established patterns in the codebase
3. **DRY (Don't Repeat Yourself)** - but don't over-abstract
4. **KISS (Keep It Simple, Stupid)** - simplest solution that works
5. **YAGNI (You Aren't Gonna Need It)** - don't add functionality until needed

### TypeScript/JavaScript Specific
- Use `const` by default, `let` only when reassignment is needed, avoid `var`
- Prefer arrow functions for callbacks and short functions
- Use template literals for string interpolation
- Use optional chaining (`?.`) and nullish coalescing (`??`)
- Leverage TypeScript's type system - avoid `any`, use `unknown` when type is truly unknown
- Use async/await over promise chains for better readability

### Python Specific
- Follow PEP 8 style guide
- Use type hints for function signatures
- Document functions with docstrings
- Use list/dict comprehensions where appropriate (but maintain readability)
- Prefer context managers (`with` statement) for resource management

### Comments and Documentation
- **When to comment:**
  - Complex algorithms or business logic
  - Non-obvious workarounds or hacks
  - Important constraints or assumptions
- **When NOT to comment:**
  - Obvious code (let the code speak for itself)
  - Redundant information
- **Use JSDoc/docstrings for public APIs:**
  ```typescript
  /**
   * Processes geospatial data and returns fusion results.
   * @param data - The input geospatial dataset
   * @param options - Processing options
   * @returns Processed fusion results
   * @throws {DataProcessingError} If input data is invalid
   */
  function processGeoData(data: GeoData, options: ProcessOptions): FusionResult {
    // Implementation
  }
  ```

---

## AI Assistant Specific Guidelines

### Working with This Codebase

#### Initial Analysis
When starting work on this project:
1. **Read this CLAUDE.md file completely** - it contains critical context
2. **Check for README.md** - provides project-specific documentation
3. **Review package.json** - understand dependencies and available scripts
4. **Explore the codebase structure** - use grep/glob to understand organization
5. **Check existing tests** - understand how features are tested

#### Making Changes
1. **Always read before writing:**
   - Never modify code you haven't read
   - Understand the existing implementation before suggesting changes

2. **Maintain consistency:**
   - Follow existing patterns in the codebase
   - Match the style of surrounding code
   - Don't introduce new patterns without good reason

3. **Be conservative with scope:**
   - Only make requested changes plus necessary related changes
   - Don't refactor code that isn't directly related to the task
   - Don't add "nice to have" features unless explicitly asked
   - Avoid over-engineering solutions

4. **Security considerations:**
   - Watch for injection vulnerabilities (SQL, command, XSS)
   - Validate and sanitize user inputs
   - Don't expose sensitive data in logs or error messages
   - Use parameterized queries for database operations
   - Be cautious with `eval()` or similar dynamic code execution

5. **Testing:**
   - Add tests for new features
   - Update tests when modifying existing features
   - Run tests before committing
   - If tests fail, fix them (don't disable or skip)

#### Using Tools Effectively
1. **Search before asking:**
   - Use Grep to find existing implementations
   - Use Glob to discover related files
   - Check git history for context on changes

2. **Read strategically:**
   - Read entry points first (index.ts, main.py, etc.)
   - Read tests to understand expected behavior
   - Read configuration to understand project setup

3. **Plan complex changes:**
   - Use TodoWrite for multi-step tasks
   - Break down large features into smaller tasks
   - Mark tasks as completed incrementally

#### Git Operations
1. **Branch management:**
   - Create branches following the naming convention
   - For Claude-generated work, use `claude/description-{sessionId}` format
   - Always develop on feature branches, never directly on main

2. **Commits:**
   - Write clear, descriptive commit messages
   - Follow conventional commit format
   - Commit logical units of work (not too large, not too small)
   - Don't commit commented-out code or debug logs

3. **Push operations:**
   - Always use `git push -u origin <branch-name>`
   - For Claude branches, ensure branch name starts with `claude/` and ends with session ID
   - Retry on network failures (up to 4 times with exponential backoff: 2s, 4s, 8s, 16s)

#### Communication
1. **Be explicit:**
   - Explain what you're doing and why
   - Reference specific files and line numbers when discussing code
   - Use format `file_path:line_number` for code references

2. **Ask when uncertain:**
   - Don't guess at requirements
   - Clarify ambiguous instructions
   - Suggest alternatives if current approach seems problematic

3. **Provide context:**
   - Explain trade-offs in technical decisions
   - Highlight potential issues or limitations
   - Suggest follow-up improvements when appropriate

#### Error Handling
1. **When encountering errors:**
   - Read and understand the error message
   - Check relevant code and configuration
   - Try the most likely fix first
   - If unsuccessful, methodically explore other possibilities

2. **When stuck:**
   - Review the error in context of the full codebase
   - Check documentation and configuration
   - Look for similar patterns in the codebase
   - Ask the user for clarification if needed

---

## Project-Specific Notes

### geofold-fusion Specific Considerations

**Project Status:** This project is in initial setup phase. As the project develops, update this section with:

- **Domain-specific knowledge:** Geospatial concepts, fusion algorithms, data formats
- **Key dependencies:** Critical libraries and their purposes
- **Performance considerations:** Optimization strategies, bottlenecks to watch for
- **Data handling:** Expected data formats, validation requirements
- **API design:** If applicable, RESTful/GraphQL conventions
- **Deployment:** Build process, environment configuration, deployment targets

### Questions to Answer as Project Develops

1. What is the primary use case for geofold-fusion?
2. What type of data does it process (geospatial, geometric, other)?
3. What are the key algorithms or processing methods?
4. Who are the end users (developers, data scientists, end users)?
5. What are the performance requirements?
6. What are the data privacy/security requirements?
7. What external services or APIs does it integrate with?

---

## Maintenance and Updates

**This document should be updated regularly:**

- When project structure changes significantly
- When new conventions or patterns are established
- When technology stack changes
- When new workflows or processes are introduced
- After major architectural decisions
- When onboarding friction is identified

**Last Updated:** 2026-01-06
**Last Updated By:** Claude AI Assistant
**Version:** 1.0.0 (Initial Creation)

---

## Resources and References

### Documentation
- [Project README](./README.md) - Main project documentation
- [API Documentation](./docs/api.md) - API reference (when created)
- [Architecture Decision Records](./docs/adr/) - Key decisions (when created)

### External Resources
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Python PEP 8](https://pep8.org/)

### Useful Commands Quick Reference
```bash
# Development
npm run dev              # Start development server
npm run build           # Build for production
npm run lint            # Run linter
npm run format          # Format code

# Testing
npm test                # Run all tests
npm run test:watch      # Run tests in watch mode
npm run test:coverage   # Run tests with coverage

# Git
git status              # Check repository status
git log --oneline -10   # View recent commits
git branch -a           # List all branches
git checkout -b name    # Create and switch to new branch

# Dependency Management
npm install             # Install dependencies
npm update              # Update dependencies
npm audit               # Check for vulnerabilities
npm outdated            # Check for outdated packages
```

---

## Contributing

When contributing to this project:

1. **Follow all conventions** outlined in this document
2. **Update documentation** when making changes
3. **Write tests** for new functionality
4. **Keep commits atomic** and well-described
5. **Be respectful** of existing code and patterns
6. **Ask questions** when uncertain
7. **Update this CLAUDE.md** if you identify improvements or missing information

---

**Note to AI Assistants:** This document is your primary reference for working with this codebase. Treat it as authoritative guidance. When in doubt, refer back to this document or ask the user for clarification. As the project evolves, help keep this document up-to-date by suggesting updates when you notice discrepancies or gaps.

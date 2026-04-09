# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# First-time setup (install deps + generate Prisma client + run migrations)
npm run setup

# Development server (Turbopack) on http://localhost:3000
npm run dev

# Production build (uses cross-env + node-compat.cjs)
npm run build

# Reset SQLite database
npm run db:reset

# Lint
npm run lint

# Run all tests
npm test

# Run a single test file
npx vitest run src/components/chat/__tests__/ChatInterface.test.tsx
```

## Environment

Copy `.env.example` to `.env`. The only required variable is:
```
ANTHROPIC_API_KEY=sk-ant-...
```
If omitted, the app falls back to a `MockLanguageModel` that generates static Counter/Form/Card components — useful for development without burning API credits.

## Coding Guidelines

# Use comments sparingly. Only comment complex code.

# The database schema is defined in @file:schema.prisma . Reference it anytime to understand the structure of database

### Virtual File System

All AI-generated code lives in an **in-memory virtual file system** (`src/lib/file-system.ts` — `VirtualFileSystem` class). Nothing is written to disk. The virtual FS is:
- Held in React state via `FileSystemContext` (`src/lib/contexts/file-system-context.tsx`)
- Serialized to JSON and stored in the Prisma `Project.data` column when a user saves
- Transformed and injected into the preview iframe via `src/lib/transform/jsx-transformer.ts`

### AI Generation Flow

1. User prompt → `POST /api/chat` (`src/app/api/chat/route.ts`)
2. `streamText` (Vercel AI SDK) calls Claude with the system prompt from `src/lib/prompts/generation.tsx`
3. Claude uses two tools:
   - `str_replace_editor` (`src/lib/tools/str-replace.ts`) — create/view/edit files in the virtual FS
   - `file_manager` (`src/lib/tools/file-manager.ts`) — rename/delete files
4. Tool calls stream back and update `FileSystemContext` in real time
5. `PreviewFrame` (`src/components/preview/PreviewFrame.tsx`) re-renders on each FS change

The model is expected to always create `/App.jsx` as the entry point and use Tailwind CSS with `@/components/...` import aliases.

### Preview Rendering

`jsx-transformer.ts` uses Babel Standalone (in-browser) to:
1. Transform JSX/TSX files to JS
2. Build a blob-URL import map for all virtual files
3. Map `react`/`react-dom` to esm.sh CDN
4. Inject everything into an `<iframe srcdoc>` sandbox

### Context System

Two React contexts coordinate the UI:
- **`FileSystemContext`** — owns the `VirtualFileSystem` instance, selected file, refresh token
- **`ChatContext`** — wraps Vercel AI SDK's `useChat`, drives tool-call side effects that mutate `FileSystemContext`

### Auth & Persistence

- JWT sessions in HTTP-only cookies (7-day expiry), managed in `src/lib/auth.ts` (server-only)
- Server actions in `src/actions/` handle sign-up/in/out and project CRUD
- Anonymous users can generate freely but cannot persist projects
- `Project` model stores `messages` (chat history) and `data` (serialized virtual FS) as JSON strings

### Database

Prisma + SQLite. Schema: `User` (email + hashed password) → many `Project` (name, messages JSON, data JSON). After schema changes run `npx prisma migrate dev`.

### Model Provider

`src/lib/provider.ts` exports a `getModel()` function. If `ANTHROPIC_API_KEY` is set it returns a Claude model (default: `claude-haiku-4-5`). Otherwise it returns the `MockLanguageModel` defined in `src/lib/prompts/generation.tsx`. The mock caps at 4 agentic steps to prevent loops.

## Testing

Tests live in `__tests__/` folders co-located with source. Vitest + jsdom + React Testing Library. Import alias `@/` works in tests via `vite-tsconfig-paths`.

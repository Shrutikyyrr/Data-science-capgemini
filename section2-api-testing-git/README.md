# Section 2 – API Testing + Git Workflow

## Postman
1. Open Postman → Import → Upload `postman_collection.json`
2. Run "Test 1 – Create Student" first (sets `student_id` variable automatically)
3. Run remaining tests in order

## Test Cases Covered
| # | Test | Expected |
|---|------|----------|
| 1 | Create student | 201 Created |
| 2 | Get by ID | 200 OK |
| 3 | Get non-existent | 404 Not Found |
| 4 | Filter by course | 200, all AI |
| 5 | Update student | 200, age=25 |
| 6 | Invalid body | 422 Unprocessable |
| 7 | Delete student | 204 No Content |

## Git Workflow
```bash
bash git_commands.sh
```
Or run commands manually from `git_commands.sh`

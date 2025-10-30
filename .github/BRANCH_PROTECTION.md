# Branch Protection Configuration

This document describes the branch protection rules for the `main` branch to ensure only administrators and repository owners can make direct changes.

## Automated Setup

If you have the [Probot Settings](https://github.com/probot/settings) app installed, it will automatically apply the settings from `.github/settings.yml`.

## Manual Setup

To manually configure branch protection in GitHub:

### 1. Navigate to Branch Protection Settings

1. Go to your repository on GitHub
2. Click **Settings** → **Branches**
3. Under "Branch protection rules", click **Add rule** or edit the existing rule for `main`

### 2. Configure Protection Rules

Set the following options to protect the main branch:

#### Basic Settings
- **Branch name pattern**: `main`

#### Protect matching branches
Check the following options:

- ✅ **Require a pull request before merging**
  - You can set "Required approvals" to 0 if you want to allow self-merging PRs
  - ✅ Check "Dismiss stale pull request approvals when new commits are pushed"

- ✅ **Require status checks to pass before merging** (if you have CI/CD)
  - ✅ Check "Require branches to be up to date before merging"

- ✅ **Restrict who can push to matching branches**
  - **Leave the users/teams list empty**
  - This ensures only repository administrators and owners can push directly
  - All other users must create pull requests

- ✅ **Do not allow bypassing the above settings**
  - Optional: Check this if you want to enforce rules even for administrators
  - Leave unchecked to allow admins/owners to bypass when necessary

- ✅ **Do not allow force pushes**
  - Prevents rewriting history on the main branch

- ✅ **Do not allow deletions**
  - Prevents accidental deletion of the main branch

### 3. Save Changes

Click **Create** or **Save changes** to apply the protection rules.

## What This Protects Against

✅ Direct pushes from non-admin users
✅ Force pushes that rewrite history
✅ Branch deletion
✅ Unreviewed changes (requires PR workflow)

## Workflow for Contributors

### For Non-Admin Users

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make changes and commit: `git commit -am "Add my feature"`
3. Push to remote: `git push origin feature/my-feature`
4. Open a Pull Request on GitHub
5. Wait for review and approval (if required)
6. Merge via GitHub interface

### For Admin/Owner Users

Admins and owners can:
- Push directly to `main` (if needed for hotfixes)
- Merge pull requests without approval
- Bypass protection rules (if `enforce_admins` is disabled)

**Best Practice**: Even admins should use the pull request workflow for transparency and code review.

## Verification

To verify the protection is working:

1. Try to push directly to main as a non-admin user:
   ```bash
   git checkout main
   git commit --allow-empty -m "test commit"
   git push origin main
   ```

   Expected result: ❌ Push rejected with error message about protected branch

2. Check the branch protection rules in GitHub Settings → Branches

## Troubleshooting

### "Required status checks are failing"
Make sure your CI/CD workflows are passing before merging.

### "Review required"
Request a review from a team member or repository collaborator.

### "Branch is out of date"
Update your branch with the latest changes from main:
```bash
git fetch origin main
git merge origin/main
```

## Additional Resources

- [GitHub Branch Protection Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

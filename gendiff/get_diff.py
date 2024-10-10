def get_diff(file1, file2):
  all_keys = sorted(set(file1.keys()).union(set(file2.keys())))
  result = []
  for key in all_keys:
      if key in file1 and key in file2:
          if file1[key] != file2[key]:
              result.append(f"- {key}: {file1[key]}")
              result.append(f"+ {key}: {file2[key]}")
          else:
              result.append(f"  {key}: {file1[key]}")
      elif key in file1:
          result.append(f"- {key}: {file1[key]}")
      elif key in file2:
          result.append(f"+ {key}: {file2[key]}")
  result = "{\n" + "\n".join(result) + "\n}"
  return result
{{ range $key, $value := . }}
  {{ range $line := $value }}
    INSERT INTO {{ $key }} VALUES ({{ $line }});
  {{ end }}
{{ end }}

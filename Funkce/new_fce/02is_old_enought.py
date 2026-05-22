def muze_hrat(vek, jmeno):
    if vek >= 12:
        return jmeno + " má povolený přístup."
    else:
        return jmeno + " je ještě moc mladý."

print(muze_hrat(14, "Adam"))
print(muze_hrat(10, "Lukáš"))
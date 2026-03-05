# Electrical Setting Wire Material Types Property

Source: https://www.revitapidocs.com/2026/dd5bc515-19eb-79b3-a5e3-2c7586b11599.htm

---

| Electrical Setting Wire Material Types Property |
| --- |

**Note: This API is now obsolete.** 

Get electrical wire material types information of the project. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("Property WireMaterialTypes is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.GetConductorMaterialIds() instead.")]
public WireMaterialTypeSet WireMaterialTypes { get; }
```

```
<ObsoleteAttribute("Property WireMaterialTypes is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.GetConductorMaterialIds() instead.")>
Public ReadOnly Property WireMaterialTypes As WireMaterialTypeSet
	Get
```

```
public:
[ObsoleteAttribute(L"Property WireMaterialTypes is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.GetConductorMaterialIds() instead.")]
property WireMaterialTypeSet^ WireMaterialTypes {
	WireMaterialTypeSet^ get ();
}
```

```
[<ObsoleteAttribute("Property WireMaterialTypes is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.GetConductorMaterialIds() instead.")>]
member WireMaterialTypes : WireMaterialTypeSet with get
```

#### Property Value

[WireMaterialTypeSet](b682dc26-30ab-9a2c-a195-dba38099d7da.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSetting Class](Electrical-Setting-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

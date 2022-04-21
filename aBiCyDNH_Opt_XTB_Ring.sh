! XTB2 Opt # invoke GFN2-XTB for Geometry Optimization
! CPCM(Acetonitrile) # initiate solvent
* xyzfile 0 1 aBiCyDNH_New.xyz
%pal
nprocs  32
end

%geom # initialize Geometric constraints for only optimizing the ring outside of the OMe groups
Constraints
{C 6 C}
{C 122 C}
{C 123 C}
{C 124 C}
{C 7 C}
{C 90 C}
{C 126 C}
{C 127 C}
{C 128 C}
{C 21 C}
{C 130 C}
{C 131 C}
{C 132 C}
{C 22 C}
{C 134 C}
{C 135 C}
{C 136 C}
{C 25 C}
{C 138 C}
{C 139 C}
{C 140 C}
{C 39 C}
{C 142 C}
{C 143 C}
{C 144 c}
{C 21 c}
{C 40 C}
{C 146 C}
{C 147 C}
{C 148 C}
{C 24 C}
{C 43 C}
{C 150 C}
{C 151 C}
{C 152 C}
{C 57 C}
{C 154 C}
{C 155 C}
{C 156 C}
{C 39 C}
{C 58 C}
{C 158 C}
{C 159 C}
{C 160 C}
{C 72 C}
{C 162 C}
{C 163 C}
{C 164 C}
{C 57 C}
{C 73 C}
{C 166 C}
{C 167 C}
{C 168 C}
{C 76 C}
{C 170 C}
{C 171 C}
{C 172 C}
{C 90 C}
{C 174 C}
{C 175 C}
{C 176 C}
{C 72 C}
{C 91 C}
{C 178 C}
{C 179 C}
{C 180 C}
{C 94 C}
{C 182 C}
{C 183 C}
{C 184 C}
{C 121 C}
{C 125 C}
{C 129 C}
{C 133 C}
{C 137 C}
{C 141 C}
{C 145 C}
{C 149 C}
{C 153 C}
{C 157 C}
{C 161 C}
{C 165 C}
{C 169 C}
{C 173 C}
{C 177 C}
{C 181 C}
end
end
